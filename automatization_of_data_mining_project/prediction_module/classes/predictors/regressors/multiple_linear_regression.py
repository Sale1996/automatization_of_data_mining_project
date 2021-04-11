from sklearn.linear_model import LinearRegression

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor


class MultipleLinearRegression(Predictor):
    def __init__(self):
        super().__init__()
        self.model: LinearRegression
        self.predictor_name: str = "Multiple Linear Regression"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.REGRESSION

    def fit(self, processed_data: PreprocessedDataSetInfo):
        regressor = LinearRegression()
        regressor.fit(processed_data.x_train, processed_data.y_train.values.ravel())

        self.model = regressor

    def predict(self, data):
        predicted_values = self.model.predict(data)
        return predicted_values

