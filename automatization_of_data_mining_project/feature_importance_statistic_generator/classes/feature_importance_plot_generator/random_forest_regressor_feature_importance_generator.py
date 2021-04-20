import numpy
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.feature_importance_plot_generator import \
    FeatureImportancePlotGenerator


class RandomForestRegressorFeatureImportanceGenerator(FeatureImportancePlotGenerator):
    def __init__(self):
        self.generator_name = 'random_forest_regressor_feature_importance'

    def generate_plot(self, preprocessed_data_set: PreprocessedDataSetInfo):
        model = RandomForestRegressor(random_state=0, n_estimators=128)
        model.fit(preprocessed_data_set.x_train, preprocessed_data_set.y_train.values.ravel())
        features = preprocessed_data_set.x_train.columns
        importances = model.feature_importances_
        indices = numpy.argsort(importances)
        plt.title('Feature Importances')
        plt.barh(range(len(indices)), importances[indices], color='b', align='center')
        plt.yticks(range(len(indices)), [features[i] for i in indices])
        plt.xlabel('Relative Importance')

        return plt