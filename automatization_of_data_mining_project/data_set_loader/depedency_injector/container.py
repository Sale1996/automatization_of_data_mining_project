from dependency_injector import containers, providers

from data_set_loader.classes.implementations.pandas_data_set_loader import PandasDataSetLoader


class Container(containers.DeclarativeContainer):
    DataSetLoader = providers.Factory(PandasDataSetLoader)