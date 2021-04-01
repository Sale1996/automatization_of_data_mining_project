from sklearn.model_selection import GridSearchCV

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor
from sklearn.ensemble import RandomForestClassifier


class RandomForestClassification(Predictor):
    def __init__(self):
        super().__init__()
        self.model: RandomForestClassifier
        self.predictor_name: str = "Random Forest Classification"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.CLASSIFICATION
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        parameters = [{'n_estimators': [10, 15, 20, 5], 'random_state': [0, 1, 2, 5], 'criterion': ['entropy']}]
        grid_search = GridSearchCV(estimator=RandomForestClassifier,
                                   param_grid=parameters,
                                   scoring='accuracy',
                                   cv=10,
                                   n_jobs=-1)
        grid_search.fit(processed_data.x_train, processed_data.y_train)
        self.best_accuracy = grid_search.best_score_
        self.best_params = grid_search.best_params_
        self.model = grid_search.best_estimator_

    def predict(self, data):
        predicted_values = self.model.predict(data)

        return predicted_values
