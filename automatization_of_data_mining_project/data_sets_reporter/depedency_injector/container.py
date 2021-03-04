from dependency_injector import containers, providers
from data_sets_reporter.classes.implementations.default_data_set_reporter import DefaultDataSetReporter


class Container(containers.DeclarativeContainer):
    DataSetReporter = providers.Factory(DefaultDataSetReporter)