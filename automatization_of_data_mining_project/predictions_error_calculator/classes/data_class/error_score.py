from dataclasses import dataclass


@dataclass
class ErrorScore(object):
    error_calculator_name: str
    error_calculator_result: float