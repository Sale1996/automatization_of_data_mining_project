import pandas
from sklearn.linear_model import LinearRegression

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.feature_importance_plot_generator import \
    FeatureImportancePlotGenerator
import matplotlib.pyplot as plt


class LinearRegressionFeatureCoefficientPlots(FeatureImportancePlotGenerator):
    def __init__(self):
        self.generator_name = 'linear_regression_feature_coefficient'

    def generate_plot(self, preprocessed_data_set: PreprocessedDataSetInfo):
        model = LinearRegression()
        model.fit(preprocessed_data_set.x_train, preprocessed_data_set.y_train.values.ravel())
        importances = pandas.DataFrame(data={
            'Attribute': preprocessed_data_set.x_train.columns,
            'Importance': model.coef_[0]
        })
        importances = importances.sort_values(by='Importance', ascending=False)

        plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
        plt.title('Feature importances obtained from coefficients', size=20)
        plt.xticks(rotation='vertical')

        return plt
