from typing import List, Tuple

import pandas

from data_set_loader.classes.pandas_data_set_loader.loader_validator.loader_validator import LoaderValidator
from data_set_loader.classes.pandas_data_set_loader.loader_validator.pathname_checker.pathname_checker import \
    PathNameChecker
from data_set_loader.exceptions.loader_exceptions import MissingImportantColumnsError


class ImportantColumnsValidator(LoaderValidator):

    def __init__(self, pathname_checker: PathNameChecker):
        self.pathname_checker = pathname_checker

    def validate_pathname(self, pathname: str):
        self.pathname_checker.check(pathname)

    def validate_loaded_data(self, loaded_data: pandas.DataFrame,
                             must_contained_columns: List[str],
                             pairs_of_must_contained_columns: List[Tuple[str, str]]):

        self.__check_are_required_columns_inside(loaded_data, must_contained_columns, pairs_of_must_contained_columns)

    def __check_are_required_columns_inside(self, loaded_data, must_contained_columns, pairs_of_must_contained_columns):
        loaded_columns = loaded_data.columns.tolist()

        for required_column in must_contained_columns:
            if required_column not in loaded_columns:
                raise MissingImportantColumnsError

        for pair in pairs_of_must_contained_columns:
            first_pair_not_contained = False

            if pair[0] not in loaded_columns:
                first_pair_not_contained = True

            second_pair_not_contained = False

            if pair[1] not in loaded_columns:
                second_pair_not_contained = True

            if first_pair_not_contained and second_pair_not_contained:
                raise MissingImportantColumnsError
