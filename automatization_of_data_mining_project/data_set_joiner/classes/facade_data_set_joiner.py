from data_set_joiner.classes.data_joiner.data_joiner import DataJoiner
from data_set_joiner.classes.data_set_joiner import DataSetsJoiner

from data_set_joiner.classes.joiner_input_validator.joiner_input_validator import JoinerInputValidator


class FacadeDataSetJoiner(DataSetsJoiner):
    def __init__(self, input_validator: JoinerInputValidator, data_joiner: DataJoiner):
        self.input_validator = input_validator
        self.data_joiner = data_joiner

    def join_data_sets(self, data_sets, joining_columns):
        self.input_validator.validate(data_sets, joining_columns)

        return self.data_joiner.join_data_sets(data_sets, joining_columns)
