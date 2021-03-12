import pandas


class CriteriaColumnValidator(object):
    def __init__(self):
        self.criteria_name = None

    def is_valid(self, data_set: pandas.DataFrame, column: str, criteria_value: int):
        pass