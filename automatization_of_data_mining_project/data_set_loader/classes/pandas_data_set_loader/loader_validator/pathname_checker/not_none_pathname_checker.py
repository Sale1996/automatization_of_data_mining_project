from data_set_loader.classes.pandas_data_set_loader.loader_validator.pathname_checker.pathname_checker import PathNameChecker
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError


class NotNonePathNameChecker(PathNameChecker):

    def check(self, pathname):
        if pathname is None:
            raise WrongPathNameFormatError
