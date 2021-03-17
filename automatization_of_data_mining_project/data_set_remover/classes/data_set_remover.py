from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove


class DataSetRemover(object):
    def remove_manually(self, data_sets_info: List[DataSetInfo], data_set_name: str):
        pass

    def remove_by_criteria(self, criteria_remover_data: DataForCriteriaRemove):
        pass

    def get_criteria_validator_names(self):
        pass