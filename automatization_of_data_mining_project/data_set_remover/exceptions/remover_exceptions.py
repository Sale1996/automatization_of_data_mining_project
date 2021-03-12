class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongInputFormatError(Error):
    pass


class NonIterableObjectError(Error):
    pass


class NonExistingDataSetWithGivenNameError(Error):
    pass


class ColumnArraysShouldNotBeBothEmpty(Error):
    pass


class ColumnArraysShouldNotBeBothFilled(Error):
    pass


class WrongCriteriaNameError(Error):
    pass


class MissingColumnToIncludeError(Error):
    pass


class MissingPercentCriteriaValueMustBeBetween1and99(Error):
    pass


class UniqueImpressionCriteriaValueMustBeGreaterThan1(Error):
    pass
