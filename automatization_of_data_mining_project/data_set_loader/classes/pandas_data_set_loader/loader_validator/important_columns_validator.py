from data_set_loader.classes.pandas_data_set_loader.loader_validator.loader_validator import LoaderValidator
from data_set_loader.classes.pandas_data_set_loader.loader_validator.pathname_checker.pathname_checker import PathNameChecker
from data_set_loader.exceptions.loader_exceptions import MissingImportantColumnsError


class ImportantColumnsValidator(LoaderValidator):

    def __init__(self, pathname_checker: PathNameChecker):
        self.pathname_checker = pathname_checker

    def validate_pathname(self, pathname):
        self.pathname_checker.check(pathname)

    def validate_loaded_data(self, loaded_data, must_contained_columns):
        self.__check_are_required_columns_inside(loaded_data, must_contained_columns)

    def __check_are_required_columns_inside(self, loaded_data, must_contained_columns):
        for required_column in must_contained_columns:
            if required_column not in loaded_data.columns.tolist():
                raise MissingImportantColumnsError

