from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo
from feature_importance_statistic_generator.classes.input_validator.input_validator import InputValidator
from feature_importance_statistic_generator.exceptions.feature_importance_generator_exceptions import \
    WrongInputFormatError


class InputValidatorImpl(InputValidator):
    def validate(self, preprocessed_data_set: PreprocessedDataSetInfo):
        if preprocessed_data_set is None:
            raise WrongInputFormatError

        if not isinstance(preprocessed_data_set, PreprocessedDataSetInfo):
            raise PreprocessedDataSetInfo
