from dependency_injector import providers

from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.classes.implementations.pandas_data_set_loader import PandasDataSetLoader

Loader: DataSetLoader = providers.Factory(PandasDataSetLoader)