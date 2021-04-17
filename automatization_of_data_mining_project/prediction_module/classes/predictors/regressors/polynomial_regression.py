from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor


class PolynomialRegression(Predictor):
    def __init__(self):
        super().__init__()
        self.model: LinearRegression
        self.predictor_name: str = "Polynomial Regression"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.REGRESSION
        self.polynomial_features = PolynomialFeatures(degree=4)
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        x_poly = self.polynomial_features.fit_transform(processed_data.x_train)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(x_poly, processed_data.y_train.values.ravel())

        self.model = lin_reg_2

    def predict(self, data):
        predicted_values = self.model.predict(self.polynomial_features.fit_transform(data))

        return predicted_values
