from dependency_injector import containers, providers

from data_set_dimension_reductioner.classes.facade_data_set_dimension_reductioner import \
    FacadeDataSetDimensionReductioner
from data_set_dimension_reductioner.classes.input_validator.input_validator_impl import InputValidatorImpl


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(InputValidatorImpl)
    data_set_dimension_reductioner = providers.Factory(FacadeDataSetDimensionReductioner, input_validator=input_validator)