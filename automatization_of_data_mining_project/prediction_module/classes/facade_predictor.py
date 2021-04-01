from typing import List

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.input_validator.input_validator import InputValidator
from prediction_module.classes.predictors.predictor import Predictor


class FacadePredictor(object):
    def __init__(self, input_validator: InputValidator,
                 predictors: List[Predictor]):
        self.input_validator = input_validator
        self.predictors = predictors

    def get_fitted_regression_predictors(self, input_data: PreprocessedDataSetInfo):
        return self.get_predictors_by_category_type(input_data, PredictorTypeEnum.REGRESSION)

    def get_fitted_classification_predictors(self, input_data: PreprocessedDataSetInfo):
        return self.get_predictors_by_category_type(input_data, PredictorTypeEnum.CLASSIFICATION)

    def get_predictors_by_category_type(self, input_data, predictor_type):
        fitted_predictors = []
        for predictor in self.predictors:
            if predictor.predictor_type == predictor_type:
                fitted_predictors.append(predictor.fit(input_data))
        return fitted_predictors

    def get_fitted_predictor_by_name(self, input_data: PreprocessedDataSetInfo, predictor_name: str):
        for predictor in self.predictors:
            if predictor.predictor_name == predictor_name:
                return predictor.fit(input_data)

    def save_predictors(self, predictors: List[Predictor], document_path: str):
        pass
