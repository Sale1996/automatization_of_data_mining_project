import pandas

from data_set_joiner.classes.joiner_input_validator.joiner_input_validator import JoinerInputValidator

from data_set_joiner.exceptions.joiner_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingJoinerColumnError


class JoinerDataFrameAndStringArrayInputValidator(JoinerInputValidator):
    def validate(self, data_sets, joining_columns):
        self.check_is_none(data_sets)
        self.check_is_none(joining_columns)
        self.check_is_iterable(data_sets)
        self.check_is_iterable(joining_columns)

        for joining_column in joining_columns:
            self.check_is_instance_of(joining_column, str)

        for data_set in data_sets:
            self.check_is_instance_of(data_set, pandas.DataFrame)
            self.check_if_data_set_contains_all_joining_columns(data_set, joining_columns)

    def check_if_data_set_contains_all_joining_columns(self, data_set, joining_columns):
        data_set_columns = data_set.columns.tolist()
        for joining_column in joining_columns:
            if joining_column not in data_set_columns:
                raise MissingJoinerColumnError

    def check_is_none(self, object):
        if object is None:
            raise WrongInputFormatError

    def check_is_iterable(self, object):
        if not isinstance(object, list):
            raise NonIterableObjectError

    def check_is_instance_of(self, object, type):
        if not isinstance(object, type):
            raise WrongInputFormatError
