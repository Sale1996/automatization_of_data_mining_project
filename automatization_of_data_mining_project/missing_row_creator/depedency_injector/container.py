from dependency_injector import containers, providers

from missing_row_creator.classes.facade_missing_row_creator import FacadeMissingRowCreator
from missing_row_creator.classes.missing_row_validator.MissingRowValidatorImpl import MissingRowValidatorImpl


class Container(containers.DeclarativeContainer):
    missing_row_validator = providers.Factory(MissingRowValidatorImpl)
    missing_row_creator = providers.Factory(FacadeMissingRowCreator, validator=missing_row_validator())
