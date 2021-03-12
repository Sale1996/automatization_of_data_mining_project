from typing import List

from data_set_remover.classes.criteria_validator.criteria_column_validator.criteria_column_validator import \
    CriteriaColumnValidator
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove


class CriteriaRemover(object):
    def __init__(self, criteria_column_validators: List[CriteriaColumnValidator]):
        self.criteria_column_validators = criteria_column_validators

    def remove_and_return_updated_list(self, criteria_remover_data: DataForCriteriaRemove):
        pass
