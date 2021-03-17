from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.criteria_validator_informer.criteria_validator_informer import CriteriaValidatorInformer
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.classes.remover.criteria_remover.criteria_remover import CriteriaRemover
from data_set_remover.classes.remover.manually_remover.manually_remover import ManuallyRemover
from data_set_remover.classes.remover_validator.criteria_remover_validator.criteria_remover_validator import \
    CriteriaRemoverValidator
from data_set_remover.classes.remover_validator.manually_remover_validator.manually_remover_validator import \
    ManuallyRemoverValidator
from data_set_remover.classes.data_set_remover import DataSetRemover


class FacadeDataSetRemover(DataSetRemover):
    def __init__(self,
                 manually_remover: ManuallyRemover, criteria_remover: CriteriaRemover,
                 manually_remover_validator: ManuallyRemoverValidator,
                 criteria_remover_validator: CriteriaRemoverValidator,
                 criteria_validator_informer: CriteriaValidatorInformer):
        self.manually_remover = manually_remover
        self.criteria_remover = criteria_remover
        self.manually_remover_validator = manually_remover_validator
        self.criteria_remover_validator = criteria_remover_validator
        self.criteria_validator_informer = criteria_validator_informer

    def remove_manually(self, data_sets_info: List[DataSetInfo], data_set_name: str):
        self.manually_remover_validator.validate(data_sets_info, data_set_name)
        return self.manually_remover.remove_and_return_updated_list(data_sets_info, data_set_name)

    def remove_by_criteria(self, criteria_remover_data: DataForCriteriaRemove):
        self.criteria_remover_validator.validate(criteria_remover_data)
        return self.criteria_remover.remove_and_return_updated_list(criteria_remover_data)

    def get_criteria_validator_names(self):
        return self.criteria_validator_informer.get_criteria_names()
