from data_set_joiner.classes.data_joiner.data_joiner import DataJoiner
from functools import reduce

import pandas


class PandasDataJoiner(DataJoiner):
    def join_data_sets(self, data_sets, joining_columns):
        df_merged = reduce(lambda left, right: pandas.merge(left, right, on=joining_columns,
                                                            how='outer'), data_sets)

        return df_merged
