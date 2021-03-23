from dependency_injector import containers, providers

from data_set_preprocessor.classes.data_set_splitter.data_set_splitter_impl import DataSetSplitterImpl
from data_set_preprocessor.classes.facade_data_set_preprocessor import FacadeDataSetPreprocessor
from data_set_preprocessor.classes.validator.data_set_processer_validator.data_set_preprocessor_validator_impl import \
    DataSetPreprocessorValidatorImpl
from data_set_preprocessor.classes.validator.data_set_spliter.data_set_splitter_validator_impl import \
    DataSetSplitterValidatorImpl


class Container(containers.DeclarativeContainer):
    data_set_preprocessor_validator = providers.Factory(DataSetPreprocessorValidatorImpl)
    data_set_splitter_validator = providers.Factory(DataSetSplitterValidatorImpl)
    data_set_splitter = providers.Factory(DataSetSplitterImpl)

    data_set_preprocessor = providers.Factory(FacadeDataSetPreprocessor,
                                              data_set_preprocessor_validator=data_set_preprocessor_validator(),
                                              data_set_splitter_validator=data_set_splitter_validator(),
                                              data_set_splitter=data_set_splitter())
