from typing import List

from data_set_remover.classes.criteria_validator.criteria_column_validator.criteria_column_validator import \
    CriteriaColumnValidator
from data_set_remover.classes.criteria_validator_informer.criteria_validator_informer import CriteriaValidatorInformer


class CriteriaValidatorInformerImpl(CriteriaValidatorInformer):
    def __init__(self, criteria_validators: List[CriteriaColumnValidator]):
        super().__init__(criteria_validators)

    def get_criteria_names(self):
        criteria_names = []

        for criteria_validator in self.criteria_validators:
            criteria_names.append(criteria_validator.criteria_name)

        return criteria_names
