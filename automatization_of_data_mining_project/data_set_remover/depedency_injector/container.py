from dependency_injector import containers, providers

from data_set_remover.classes.criteria_validator.criteria_column_validator.missing_data_percent_criteria_column_validator import \
    MissingDataPercentCriteriaColumnValidator
from data_set_remover.classes.criteria_validator.criteria_column_validator.number_of_unique_impressions_criteria_column_validator import \
    NumberOfUniqueImpressionsCriteriaColumnValidator
from data_set_remover.classes.criteria_validator.criteria_value_validator.missing_data_percent_criteria_value_validator import \
    MissingDataPercentCriteriaValueValidator
from data_set_remover.classes.criteria_validator.criteria_value_validator.number_of_unique_impressions_criteria_value_validator import \
    NumberOfUniqueImpressionsCriteriaValueValidator
from data_set_remover.classes.criteria_validator_informer.criteria_validator_informer_impl import \
    CriteriaValidatorInformerImpl
from data_set_remover.classes.facade_data_set_remover import FacadeDataSetRemover
from data_set_remover.classes.remover.criteria_remover.criteria_remover_impl import CriteriaRemoverImpl
from data_set_remover.classes.remover.manually_remover.delete_by_name_remover import DeleteByNameRemover
from data_set_remover.classes.remover_validator.criteria_remover_validator.criteria_remover_validator_impl import \
    CriteriaRemoverValidatorImpl
from data_set_remover.classes.remover_validator.manually_remover_validator.delete_by_name_remover_validator import \
    DeleteByNameRemoverValidator


class Container(containers.DeclarativeContainer):
    manually_remover_validator = providers.Factory(DeleteByNameRemoverValidator)
    manually_remover = providers.Factory(DeleteByNameRemover)

    missing_data_percent_criteria_value_validator = providers.Factory(MissingDataPercentCriteriaValueValidator)
    number_of_unique_impressions_criteria_validator = providers.Factory(NumberOfUniqueImpressionsCriteriaValueValidator)

    missing_data_percent_criteria_column_validator = providers.Factory(MissingDataPercentCriteriaColumnValidator,
                                                                       criteria_value_validator=missing_data_percent_criteria_value_validator())
    number_of_unique_impressions_criteria_column_validator = providers.Factory(
        NumberOfUniqueImpressionsCriteriaColumnValidator,
        criteria_value_validator=number_of_unique_impressions_criteria_validator())
    criteria_remover_validator = providers.Factory(CriteriaRemoverValidatorImpl,
                                                   criteria_column_validators=[
                                                       missing_data_percent_criteria_column_validator(),
                                                       number_of_unique_impressions_criteria_column_validator()])
    criteria_remover = providers.Factory(CriteriaRemoverImpl,
                                         criteria_column_validators=[missing_data_percent_criteria_column_validator(),
                                                                     number_of_unique_impressions_criteria_column_validator()])

    criteria_validator_informer = providers.Factory(CriteriaValidatorInformerImpl,
                                                    criteria_validators=[
                                                        missing_data_percent_criteria_column_validator(),
                                                        number_of_unique_impressions_criteria_column_validator()])

    data_set_remover = providers.Factory(FacadeDataSetRemover,
                                         manually_remover=manually_remover(),
                                         criteria_remover=criteria_remover(),
                                         manually_remover_validator=manually_remover_validator(),
                                         criteria_remover_validator=criteria_remover_validator(),
                                         criteria_validator_informer=criteria_validator_informer())
