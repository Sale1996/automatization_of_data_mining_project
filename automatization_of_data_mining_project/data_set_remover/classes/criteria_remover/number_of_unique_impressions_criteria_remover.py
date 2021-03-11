from data_set_remover.classes.criteria_remover.criteria_remover import CriteriaRemover
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove


class NumberOfUniqueImpressionsCriteriaRemover(CriteriaRemover):
    def __init__(self):
        super().__init__()
        self.criteria_name = "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA"

    def remove_data_sets_by_criteria(self, data: DataForCriteriaRemove):
        pass
