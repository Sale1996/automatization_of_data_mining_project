from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.model_selection import GridSearchCV

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor


class ElasticRegression(Predictor):
    def __init__(self):
        super().__init__()
        self.model: ElasticNet
        self.predictor_name: str = "Elastic Regression"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.REGRESSION
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        parameters = [{'alpha': [0.001, 0.01, 0.1, 0.8]}]
        grid_search = GridSearchCV(estimator=ElasticNet(),
                                   param_grid=parameters,
                                   scoring='r2',
                                   cv=10,
                                   n_jobs=-1)
        grid_search.fit(processed_data.x_train, processed_data.y_train.values.ravel())

        self.best_accuracy = grid_search.best_score_
        self.best_params = grid_search.best_params_
        self.model = grid_search.best_estimator_

    def predict(self, data):
        predicted_values = self.model.predict(data)
        return predicted_values
