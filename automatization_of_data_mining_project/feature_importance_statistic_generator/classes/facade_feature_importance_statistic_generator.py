from datetime import datetime
from typing import List

import matplotlib.pyplot as plt

from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.feature_importance_plot_generator.feature_importance_plot_generator import \
    FeatureImportancePlotGenerator
from feature_importance_statistic_generator.classes.feature_importance_statistic_generator import \
    FeatureImportanceStatisticGenerator
from feature_importance_statistic_generator.classes.input_validator.input_validator import InputValidator


class FacadeFeatureImportanceStatisticGenerator(FeatureImportanceStatisticGenerator):
    def __init__(self, input_validator: InputValidator,
                 plot_generators: List[FeatureImportancePlotGenerator]):
        self.input_validator = input_validator
        self.plot_generators = plot_generators

    def generate_feature_importance_statistics(self, preprocessed_data_set: PreprocessedDataSetInfo,
                                               save_path: str):
        self.input_validator.validate(preprocessed_data_set)
        current_time_string = self.get_current_date_time_as_string()

        for plot_generator in self.plot_generators:
            generated_plot: plt = plot_generator.generate_plot(preprocessed_data_set)
            generated_plot.show()
            generated_plot.savefig(save_path + '/feature_importance_plt_' + plot_generator.generator_name + '_' + current_time_string + '.png')

    def get_current_date_time_as_string(self):
        current_time = datetime.now()
        current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
        return current_time_string

