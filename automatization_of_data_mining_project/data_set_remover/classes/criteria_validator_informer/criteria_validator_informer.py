from typing import List

from data_set_remover.classes.criteria_validator.criteria_column_validator.criteria_column_validator import \
    CriteriaColumnValidator


class CriteriaValidatorInformer(object):
    def __init__(self, criteria_validators: List[CriteriaColumnValidator]):
        self.criteria_validators = criteria_validators

    def get_criteria_names(self):
        pass
