from dependency_injector import containers, providers

from data_set_loader.classes.pandas_data_set_loader.loader.data_frame_with_columns_array_loader import \
    DataFrameWithColumnsArrayLoader
from data_set_loader.classes.pandas_data_set_loader.loader_validator.important_columns_validator import \
    ImportantColumnsValidator
from data_set_loader.classes.pandas_data_set_loader.loader.pandas_reader.csv_excel_pandas_reader import CsvExcelPandasReader
from data_set_loader.classes.pandas_data_set_loader.loader_validator.pathname_checker.not_none_pathname_checker import NotNonePathNameChecker
from data_set_loader.classes.pandas_data_set_loader.facade_pandas_data_set_loader import FacadePandasDataSetLoader
from data_set_loader.classes.pandas_data_set_loader.processor.converter.document_converter.document_column_pair_converter import \
    DocumentColumnPairConverter
from data_set_loader.classes.pandas_data_set_loader.processor.data_processor_for_pair_of_must_contained_columns import \
    DataProcessorForPairOfMustContainedColumns


class Container(containers.DeclarativeContainer):
    # loader
    pandas_reader = providers.Factory(CsvExcelPandasReader)
    data_loader = providers.Factory(DataFrameWithColumnsArrayLoader, pandas_reader=pandas_reader)
    # validator
    pathname_checker = providers.Factory(NotNonePathNameChecker)
    validator = providers.Factory(ImportantColumnsValidator, pathname_checker=pathname_checker)
    # data processor
    column_pair_converter = providers.Factory(DocumentColumnPairConverter, loader=data_loader)
    data_processor = providers.Factory(
        DataProcessorForPairOfMustContainedColumns, column_pair_converter=column_pair_converter)

    data_set_loader = providers.Factory(
        FacadePandasDataSetLoader, data_loader=data_loader, validator=validator, data_processor=data_processor)
