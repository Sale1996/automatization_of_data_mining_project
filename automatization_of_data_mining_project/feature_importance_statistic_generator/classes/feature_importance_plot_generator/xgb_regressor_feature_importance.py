import pandas
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.feature_importance_plot_generator import \
    FeatureImportancePlotGenerator


class XGBRegressorFeatureImportance(FeatureImportancePlotGenerator):
    def __init__(self):
        self.generator_name = 'xgb_regressor_feature_importance'

    def generate_plot(self, preprocessed_data_set: PreprocessedDataSetInfo):
        model = XGBRegressor()
        model.fit(preprocessed_data_set.x_train, preprocessed_data_set.y_train)
        importances = pandas.DataFrame(data={
            'Attribute': preprocessed_data_set.x_train.columns,
            'Importance': model.feature_importances_
        })
        importances = importances.sort_values(by='Importance', ascending=False)

        plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
        plt.title('Feature importances obtained from coefficients', size=20)
        plt.xticks(rotation='vertical')

        return plt
