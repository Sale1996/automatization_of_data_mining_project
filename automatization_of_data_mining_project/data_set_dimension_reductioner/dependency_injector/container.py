from dependency_injector import containers, providers

from data_set_dimension_reductioner.classes.facade_data_set_dimension_reductioner import \
    FacadeDataSetDimensionReductioner
from data_set_dimension_reductioner.classes.input_validator.dimension_reduction.input_validator_for_dimension_reduction import \
    InputValidatorForDimensionReduction
from data_set_dimension_reductioner.classes.input_validator.dimension_reduction_statistics.input_validator_for_dimension_reduction_statistics_impl import \
    InputValidatorForDimensionReductionStatisticsImpl


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(InputValidatorForDimensionReduction)
    input_validator_for_dimension_reduction_statistics = providers.Factory(
        InputValidatorForDimensionReductionStatisticsImpl)

    data_set_dimension_reductioner = providers.Factory(FacadeDataSetDimensionReductioner,
                                                       input_validator=input_validator,
                                                       dimension_reduction_statistics_reporter=input_validator_for_dimension_reduction_statistics)
