from typing import List

from data_set_dimension_reductioner import DimensionReducer
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.factor_analysis_parameters import \
    FactorAnalysisParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.low_variance_filter_parameters import \
    LowVarianceFilterParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.pca_parameters import \
    PCAParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.random_forest_parameters import \
    RandomForestParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.factor_analysis_dimension_reduction import \
    FactorAnalysisDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.low_variance_filter_dimension_reduction import \
    LowVarianceFilterDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.pca_dimension_reduction import PCADimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.random_forest_dimension_reduction import \
    RandomForestDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction_statistics_reporter.document_statistic_reporter import \
    DimensionReductionDocumentStatisticReporter
from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo


def get_dimensionality_reduced_data_sets(preprocessed_data_set: PreprocessedDataSetInfo):
    # low variance filter dimension reductioners
    lvf_threshold_20_percent = LowVarianceFilterParameters(20)
    lvf_threshold_40_percent = LowVarianceFilterParameters(40)
    lvf_threshold_60_percent = LowVarianceFilterParameters(60)
    lvf_threshold_80_percent = LowVarianceFilterParameters(80)
    low_variance_dimension_reduction = LowVarianceFilterDimensionReduction(parameters=[lvf_threshold_20_percent,
                                                                                       lvf_threshold_40_percent,
                                                                                       lvf_threshold_60_percent,
                                                                                       lvf_threshold_80_percent])

    # random forest parameters with different number of features
    rf_5_features = RandomForestParameters(5, 1, 10)
    rf_15_features = RandomForestParameters(15, 1, 10)
    rf_25_features = RandomForestParameters(25, 1, 10)
    random_forest_dimension_reduction = RandomForestDimensionReduction(parameters=[rf_5_features,
                                                                                   rf_15_features,
                                                                                   rf_25_features])

    # pca parameters with different number of desired reduced columns (25%, 50%, 75%)
    pca_25_percent_columns = PCAParameters(round(preprocessed_data_set.x_test.shape[1]*0.25))
    pca_50_percent_columns = PCAParameters(round(preprocessed_data_set.x_test.shape[1]*0.5))
    pca_75_percent_columns = PCAParameters(round(preprocessed_data_set.x_test.shape[1]*0.75))
    pca_dimension_reduction = PCADimensionReduction(parameters=[pca_25_percent_columns,
                                                                pca_50_percent_columns,
                                                                pca_75_percent_columns])

    # factor analysis with different number of desired reduced columns (25%, 50%, 75%)
    fa_25_percent_columns = FactorAnalysisParameters(round(preprocessed_data_set.x_test.shape[1]*0.25))
    fa_50_percent_columns = FactorAnalysisParameters(round(preprocessed_data_set.x_test.shape[1]*0.50))
    fa_75_percent_columns = FactorAnalysisParameters(round(preprocessed_data_set.x_test.shape[1]*0.75))
    factor_analysis_dimension_reduction = FactorAnalysisDimensionReduction(parameters=[fa_25_percent_columns,
                                                                                       fa_50_percent_columns,
                                                                                       fa_75_percent_columns])

    statistic_reporter = DimensionReductionDocumentStatisticReporter(
        "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics/dimension_reduction_statistics")

    data_set_dimension_reductioner = DimensionReducer(
        dimension_reductioners=[low_variance_dimension_reduction,
                                random_forest_dimension_reduction,
                                pca_dimension_reduction,
                                factor_analysis_dimension_reduction],
        statistic_reporter=statistic_reporter
    )

    print("\n#Reduce train part of data set with all dimension reductions")
    train_dimension_reduction_results: List[
        DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(preprocessed_data_set.x_train,
                                                                                         preprocessed_data_set.y_train)

    data_set_dimension_reductioner.create_dimension_reduction_statistics(train_dimension_reduction_results)

    print("\n#Reduce test part of data set with all dimension reductions\n")
    test_dimension_reduction_results: List[
        DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(preprocessed_data_set.x_test,
                                                                                         preprocessed_data_set.y_test)

    return train_dimension_reduction_results, test_dimension_reduction_results


