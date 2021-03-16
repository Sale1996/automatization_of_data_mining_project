from dependency_injector import containers, providers

from data_set_slicer.classes.facade_data_set_slicer import FacadeDataSetSlicer
from data_set_slicer.classes.validator.iterable_data_set_info_validator import IterableDataSetInfoValidator


class Container(containers.DeclarativeContainer):
    data_slicer_validator = providers.Factory(IterableDataSetInfoValidator)
    data_set_slicer = providers.Factory(FacadeDataSetSlicer, validator=data_slicer_validator())
