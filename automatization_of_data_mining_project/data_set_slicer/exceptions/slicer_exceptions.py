class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongInputFormatError(Error):
    pass


class NonIterableObjectError(Error):
    pass


class NonExistingSlicingMethodError(Error):
    pass


class EmptyResultsError(Error):
    pass


class WrongRangeObjectFormatError(Error):
    pass