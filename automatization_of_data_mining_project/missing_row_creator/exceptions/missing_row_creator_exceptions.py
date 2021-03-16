class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongInputFormatError(Error):
    pass


class NonIterableObjectError(Error):
    pass


class MissingYearColumnError(Error):
    pass


class MissingCountryCodeColumnError(Error):
    pass
