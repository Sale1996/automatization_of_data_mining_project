from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


class RandomForestRegression(Predictor):
    def __init__(self):
        super().__init__()
        self.model: RandomForestRegressor
        self.predictor_name: str = "Random Forest Regression"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.REGRESSION
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        parameters = [{'n_estimators': [10, 15, 20, 5], 'random_state': [0, 1, 2, 5]}]
        grid_search = GridSearchCV(estimator=RandomForestRegressor(),
                                   param_grid=parameters,
                                   scoring='r2',
                                   cv=10,
                                   n_jobs=-1)
        grid_search.fit(processed_data.x_train, processed_data.y_train.values.ravel())
        self.best_params = grid_search.best_params_
        self.best_accuracy = grid_search.best_score_
        self.model = grid_search.best_estimator_

    def predict(self, data):
        predicted_values = self.model.predict(data)

        return predicted_values
