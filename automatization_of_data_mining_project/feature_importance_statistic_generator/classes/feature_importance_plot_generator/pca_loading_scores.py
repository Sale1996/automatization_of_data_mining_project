import numpy
import pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.feature_importance_plot_generator import \
    FeatureImportancePlotGenerator


class PCALoadingScores(FeatureImportancePlotGenerator):
    def __init__(self):
        self.generator_name = 'pca_loading_scores'

    def generate_plot(self, preprocessed_data_set: PreprocessedDataSetInfo):
        pca = PCA().fit(preprocessed_data_set.x_train)
        loadings = pandas.DataFrame(
            data=pca.components_.T * numpy.sqrt(pca.explained_variance_),
            columns=[f'PC{i}' for i in range(1, len(preprocessed_data_set.x_train.columns) + 1)],
            index=preprocessed_data_set.x_train.columns
        )
        pc1_loadings = loadings.sort_values(by='PC1', ascending=False)[['PC1']]
        pc1_loadings = pc1_loadings.reset_index()
        pc1_loadings.columns = ['Attribute', 'CorrelationWithPC1']

        plt.bar(x=pc1_loadings['Attribute'], height=pc1_loadings['CorrelationWithPC1'], color='#087E8B')
        plt.title('PCA loading scores (first principal component)', size=20)
        plt.xticks(rotation='vertical')

        return plt
