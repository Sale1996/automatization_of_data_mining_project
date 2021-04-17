import numpy
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_predict

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor


class PCARegression(Predictor):
    def __init__(self):
        super().__init__()
        self.model: LinearRegression
        self.predictor_name: str = "PCA Regression"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.REGRESSION
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        number_of_columns = processed_data.x_train.shape[1]
        mse = []
        component = numpy.arange(1, number_of_columns)
        for i in component:
            pls = PLSRegression(n_components=i)
            y_cv = cross_val_predict(pls, processed_data.x_train, processed_data.y_train, cv=10)
            mse.append(mean_squared_error(processed_data.y_train, y_cv))

        # Calculate and print the position of minimum in MSE
        msemin = numpy.argmin(mse)

        # Define PLS object with optimal number of components
        regressor = PLSRegression(n_components=msemin + 1)
        regressor.fit(processed_data.x_train, processed_data.y_train)
        self.model = regressor

    def predict(self, data):
        predicted_values = self.model.predict(data)
        return predicted_values
