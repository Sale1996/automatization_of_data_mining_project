from dataclasses import dataclass

import pandas


@dataclass
class PreprocessedDataSetInfo(object):
    x_train: pandas.DataFrame
    x_test: pandas.DataFrame
    y_train: pandas.DataFrame
    y_test: pandas.DataFrame
