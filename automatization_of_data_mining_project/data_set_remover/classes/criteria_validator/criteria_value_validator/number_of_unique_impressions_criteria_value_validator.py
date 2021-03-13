from data_set_remover.classes.criteria_validator.criteria_value_validator.criteria_value_validator import \
    CriteriaValueValidator
from data_set_remover.exceptions.remover_exceptions import UniqueImpressionCriteriaValueMustBeGreaterThan1


class NumberOfUniqueImpressionsCriteriaValueValidator(CriteriaValueValidator):
    def is_valid(self, value: int):
        if value < 1:
            raise UniqueImpressionCriteriaValueMustBeGreaterThan1
