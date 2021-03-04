class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongPathNameFormatError(Error):
    """Raised when the path name has wrong format"""
    pass


class FileIsNotFoundError(Error):
    """Raised when the input file from the path name was not found by loader"""
    pass


class MissingImportantColumnsError(Error):
    """Raised when the loaded data set has missing one or more of the important columns"""
    pass
