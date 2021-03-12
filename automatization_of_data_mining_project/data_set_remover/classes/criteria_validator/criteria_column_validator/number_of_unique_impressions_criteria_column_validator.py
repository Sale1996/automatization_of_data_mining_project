import pandas

from data_set_remover.classes.criteria_validator.criteria_column_validator.criteria_column_validator import \
    CriteriaColumnValidator


class NumberOfUniqueImpressionsCriteriaColumnValidator(CriteriaColumnValidator):
    def __init__(self):
        super().__init__()
        self.criteria_name = "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA"

    def is_valid(self, data_set: pandas.DataFrame, column: str, criteria_value: int):
        unique_values = self.calculate_number_of_unique_impressions(column, data_set)

        if unique_values < criteria_value:
            return False
        else:
            return True

    def calculate_number_of_unique_impressions(self, column, data_set):
        return data_set[column].value_counts().size
