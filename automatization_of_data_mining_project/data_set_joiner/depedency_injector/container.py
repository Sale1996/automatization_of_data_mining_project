from dependency_injector import containers, providers

from data_set_joiner.classes.data_joiner.pandas_data_joiner import PandasDataJoiner
from data_set_joiner.classes.facade_data_set_joiner import FacadeDataSetJoiner
from data_set_joiner.classes.joiner_input_validator.joiner_data_frame_and_string_array_input_validator import \
    JoinerDataFrameAndStringArrayInputValidator


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(JoinerDataFrameAndStringArrayInputValidator)
    data_joiner = providers.Factory(PandasDataJoiner)
    data_sets_joiner = providers.Factory(FacadeDataSetJoiner, input_validator=input_validator, data_joiner=data_joiner)
