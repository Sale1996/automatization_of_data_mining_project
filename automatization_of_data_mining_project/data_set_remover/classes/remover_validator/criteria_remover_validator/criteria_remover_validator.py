from typing import List

from data_set_remover.classes.criteria_validator.criteria_value_validator.criteria_value_validator import \
    CriteriaValueValidator
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove


class CriteriaRemoverValidator(object):
    def __init__(self, criteria_value_validators: List[CriteriaValueValidator]):
        self.criteria_value_validators = criteria_value_validators

    def validate(self, criteria_remover_data: DataForCriteriaRemove):
        pass