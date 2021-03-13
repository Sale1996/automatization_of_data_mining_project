import pandas

from data_set_remover.classes.criteria_validator.criteria_column_validator.criteria_column_validator import \
    CriteriaColumnValidator
from data_set_remover.classes.criteria_validator.criteria_value_validator.criteria_value_validator import \
    CriteriaValueValidator


class MissingDataPercentCriteriaColumnValidator(CriteriaColumnValidator):
    def __init__(self, criteria_value_validator: CriteriaValueValidator):
        super().__init__(criteria_value_validator)
        self.criteria_name = "MISSING_DATA_PERCENT_CRITERIA"

    def is_valid(self, data_set: pandas.DataFrame, column: str, criteria_value: int):
        percent_of_missing_data = self.__calculate_missing_percent_of_data(column, data_set)

        if percent_of_missing_data > criteria_value:
            return False
        else:
            return True

    def __calculate_missing_percent_of_data(self, column, data_set):
        total_number_of_data = data_set[column].shape[0]
        total_number_of_missing_data = data_set[column].isnull().sum()
        percent_of_missing_data = round(total_number_of_missing_data / total_number_of_data * 100, 2)
        return percent_of_missing_data
