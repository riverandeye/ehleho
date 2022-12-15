class Error(Exception):
    """Base class for all exceptions in this module."""
    
    pass

class EndsWithInvalidWordException(Exception):
    """Exception raised when the end of a string is not a suffix of another."""

    def __init__(self, end_word):
        self.end = end_word
        super(EndsWithInvalidWordException, self).__init__()