from dataclasses import dataclass
from typing import List

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.predictors.predictor import Predictor
from predictions_error_calculator.classes.data_class.error_score import ErrorScore


@dataclass
class PredictionScore(object):
    preprocessed_data_frame: PreprocessedDataSetInfo
    dimension_reduction_name: str
    predictor: Predictor
    error_scores: List[ErrorScore]
