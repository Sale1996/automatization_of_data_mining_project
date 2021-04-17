from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum


class Predictor(object):
    def __init__(self):
        self.model = None
        self.predictor_name: str = None
        self.predictor_type: PredictorTypeEnum = None
        self.best_params = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        pass

    def predict(self, data):
        pass
