class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongInputFormatError(Error):
    pass


class NonIterableObjectError(Error):
    pass


class MissingFirstColumnPairError(Error):
    pass


class MissingSecondColumnPairError(Error):
    pass


