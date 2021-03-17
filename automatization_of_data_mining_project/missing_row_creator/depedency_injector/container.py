from dependency_injector import containers, providers

from missing_row_creator.classes.facade_missing_row_creator import FacadeMissingRowCreator
from missing_row_creator.classes.missing_row_validator.MissingRowValidatorImpl import MissingRowValidatorImpl
from missing_row_creator.classes.missing_values_pair_map_creator.missing_pair_values_map_creator_impl import \
    MissingPairValuesMapCreatorImpl
from missing_row_creator.classes.row_creator.row_creator_impl import RowCreatorImpl


class Container(containers.DeclarativeContainer):
    missing_row_validator = providers.Factory(MissingRowValidatorImpl)
    missing_pair_values_map_creator = providers.Factory(MissingPairValuesMapCreatorImpl)
    row_creator = providers.Factory(RowCreatorImpl)
    missing_row_creator = providers.Factory(FacadeMissingRowCreator, validator=missing_row_validator(),
                                            missing_pair_values_map_creator=missing_pair_values_map_creator(),
                                            row_creator=row_creator())
