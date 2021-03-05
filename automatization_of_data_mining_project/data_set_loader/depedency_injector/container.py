from dependency_injector import containers, providers

from data_set_loader.classes.pandas_data_set_loader.pandas_reader.csv_excel_pandas_reader import CsvExcelPandasReader
from data_set_loader.classes.pandas_data_set_loader.pathname_checker.not_none_pathname_checker import NotNonePathNameChecker
from data_set_loader.classes.pandas_data_set_loader.pandas_data_set_loader import PandasDataSetLoader


class Container(containers.DeclarativeContainer):
    pandas_reader = providers.Factory(CsvExcelPandasReader)
    pathname_checker = providers.Factory(NotNonePathNameChecker)
    data_set_loader = providers.Factory(
        PandasDataSetLoader, pandas_reader=pandas_reader, pathname_checker=pathname_checker)
