from sklearn.model_selection import GridSearchCV

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from prediction_module.classes.data_class.predictor_type_enum import PredictorTypeEnum
from prediction_module.classes.predictors.predictor import Predictor
from sklearn.svm import SVC


class SupportVectorMachine(Predictor):
    def __init__(self):
        super().__init__()
        self.model: SVC
        self.predictor_name: str = "Support Vector Machine"
        self.predictor_type: PredictorTypeEnum = PredictorTypeEnum.CLASSIFICATION
        self.best_params = None
        self.best_accuracy = None

    def fit(self, processed_data: PreprocessedDataSetInfo):
        parameters = [{'C': [0.25, 0.5, 0.75, 1], 'kernel': ['linear']},
                      {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['rbf'],
                       'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}]
        grid_search = GridSearchCV(estimator=SVC,
                                   param_grid=parameters,
                                   scoring='accuracy',
                                   cv=10,
                                   n_jobs=-1)
        grid_search.fit(processed_data.x_train, processed_data.y_train)
        self.best_params = grid_search.best_params_
        self.best_accuracy = grid_search.best_score_
        self.model = grid_search.best_estimator_

    def predict(self, data):
        predicted_values = self.model.predict(data)

        return predicted_values
