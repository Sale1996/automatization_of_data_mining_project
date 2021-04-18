import csv
import os
from datetime import datetime
from typing import List

import pandas
from termcolor import colored

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator import FeatureImportanceGenerator
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.linear_regression_feature_coefficient_plots import \
    LinearRegressionFeatureCoefficientPlots
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.pca_loading_scores import \
    PCALoadingScores
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.random_forest_regressor_feature_importance_generator import \
    RandomForestRegressorFeatureImportanceGenerator
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.xgb_regressor_feature_importance import \
    XGBRegressorFeatureImportance
from main_functionality.create_predicitve_models_sub_functionality.get_data_sets_with_filled_nan_values import \
    get_data_sets_with_filled_nan_values
from main_functionality.create_predicitve_models_sub_functionality.get_dimensionality_reduced_data_sets import \
    get_dimensionality_reduced_data_sets
from main_functionality.create_predicitve_models_sub_functionality.get_joined_data_set import get_joined_data_set
from main_functionality.create_predicitve_models_sub_functionality.get_preprocessed_data_frame import \
    get_preprocessed_data_frame
from main_functionality.create_predicitve_models_sub_functionality.get_sliced_data_sets import \
    get_loaded_data_sets_in_year_range_with_filled_rows
from main_functionality.data_class.prediction_score import PredictionScore
from prediction_module import PredictorFactory
from prediction_module.classes.predictors.predictor import Predictor
from predictions_error_calculator import ErrorCalculator
from predictions_error_calculator.classes.data_class.error_score import ErrorScore
from predictions_error_calculator.classes.error_calculator.mse_error_calculator import MeanSquareErrorCalculator
from predictions_error_calculator.classes.error_calculator.r2_error_calculator import R2ErrorCalculator

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def create_predictive_model_and_create_statistics(loaded_data_sets: List[DataSetInfo]):
    # slice data sets
    sliced_data_sets_in_year_range = get_loaded_data_sets_in_year_range_with_filled_rows(loaded_data_sets)

    if sliced_data_sets_in_year_range == ERROR_RETURN_VALUE:
        return ERROR_RETURN_VALUE

    # fill nan values
    data_sets_with_filled_nan_values = get_data_sets_with_filled_nan_values(sliced_data_sets_in_year_range)

    if data_sets_with_filled_nan_values == ERROR_RETURN_VALUE:
        return ERROR_RETURN_VALUE

    # join all data sets
    joined_data_frame = get_joined_data_set(data_sets_with_filled_nan_values)

    # preprocess joined data set
    preprocessed_joined_data_frame, predictor_column_type = get_preprocessed_data_frame(joined_data_frame)

    # generate dimension reduction models
    train_dimension_reduction_results, test_dimension_reduction_results = get_dimensionality_reduced_data_sets(
        preprocessed_joined_data_frame)

    reduced_data_set_with_prediction_model: List[PredictionScore] = []

    # append not reduced data set too
    not_reduced_train_data_set = DimensionReductionResult("Original data set",
                                                          preprocessed_joined_data_frame.x_train.values,
                                                          1, 1)

    not_reduced_test_data_set = DimensionReductionResult("Original data set",
                                                         preprocessed_joined_data_frame.x_test.values,
                                                         1, 1)

    train_dimension_reduction_results.append(not_reduced_train_data_set)
    test_dimension_reduction_results.append(not_reduced_test_data_set)

    # iterate thought every dimension reductioned data set
    for i in range(0, len(train_dimension_reduction_results)):
        predictor_factory = PredictorFactory()
        train_data_frame = pandas.DataFrame(train_dimension_reduction_results[i].reduced_data_set)
        test_data_frame = pandas.DataFrame(test_dimension_reduction_results[i].reduced_data_set)
        dimension_reductioned_preprocessed_data_frame = PreprocessedDataSetInfo(train_data_frame,
                                                                                test_data_frame,
                                                                                preprocessed_joined_data_frame.y_train,
                                                                                preprocessed_joined_data_frame.y_test)

        # ovde trebam da pitam da li je regresija ili klasifikacija!

        if predictor_column_type == "numerical_value":
            print("##Fitting regression predictors for data set reduced with " + train_dimension_reduction_results[
                i].reduction_name)
            list_of_predictors: List[Predictor] = predictor_factory.get_fitted_regression_predictors(
                dimension_reductioned_preprocessed_data_frame)
        elif predictor_column_type == "categorical_value":
            print("##Fitting classification predictors for data set reduced with " + train_dimension_reduction_results[
                i].reduction_name)
            list_of_predictors: List[Predictor] = predictor_factory.get_fitted_classification_predictors(
                dimension_reductioned_preprocessed_data_frame)
        else:
            ERROR_RETURN_VALUE

        for predictor_instance in list_of_predictors:
            prediction_score_object = PredictionScore(dimension_reductioned_preprocessed_data_frame,
                                                      train_dimension_reduction_results[i].reduction_name,
                                                      predictor_instance,
                                                      None)

            reduced_data_set_with_prediction_model.append(prediction_score_object)

    mse_error_calculator = MeanSquareErrorCalculator()
    r2_error_calculator = R2ErrorCalculator()

    predictions_error_calculator = ErrorCalculator(error_calculators=[mse_error_calculator, r2_error_calculator])

    # calculate predictor error and then insert into object
    for prediction_score_object in reduced_data_set_with_prediction_model:
        predicted_values = prediction_score_object.predictor.predict(
            prediction_score_object.preprocessed_data_frame.x_test)

        actual_values = prediction_score_object.preprocessed_data_frame.y_test.values.flatten()

        error_scores: List[ErrorScore] = predictions_error_calculator.calculate_errors(
            actual_values.tolist(),
            predicted_values.tolist())

        prediction_score_object.error_scores = error_scores

    # generate document with all results
    error_information_for_document = []

    for prediction_score_object in reduced_data_set_with_prediction_model:
        names_row = []
        values_row = []

        names_row.append("Dimension reduction + parameters")
        values_row.append(prediction_score_object.dimension_reduction_name)

        names_row.append("Prediction model + parameters")
        predictor_value = prediction_score_object.predictor.predictor_name
        predictor_value += " | Parameters: "
        if prediction_score_object.predictor.best_params is None:
            predictor_value += "default"
        else:
            for param_name in prediction_score_object.predictor.best_params:
                predictor_value += param_name + '=' + str(prediction_score_object.predictor.best_params[param_name]) + ';'
        values_row.append(predictor_value)

        for error_object in prediction_score_object.error_scores:
            names_row.append(error_object.error_calculator_name)
            values_row.append(error_object.error_calculator_result)

        error_information_for_document.append(names_row)
        error_information_for_document.append(values_row)
        error_information_for_document.append([""])

    path = "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics/final_results"
    current_time = datetime.now()
    current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
    filename = os.path.join(
        path + "/final_results_" + current_time_string + ".csv")
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(error_information_for_document)

    print("Gotovo")

    linear_regression_feature_coefficient = LinearRegressionFeatureCoefficientPlots()
    pca_loading_scores = PCALoadingScores()
    random_forest_regressor_feature_importance = RandomForestRegressorFeatureImportanceGenerator()
    xgb_regressor_feature_importance = XGBRegressorFeatureImportance()

    feature_importance_generator = FeatureImportanceGenerator(plot_generators=[linear_regression_feature_coefficient,
                                                                               pca_loading_scores,
                                                                               random_forest_regressor_feature_importance,
                                                                               xgb_regressor_feature_importance])

    feature_importance_generator.generate_feature_importance_statistics(preprocessed_joined_data_frame, path)

    return ERROR_RETURN_VALUE
