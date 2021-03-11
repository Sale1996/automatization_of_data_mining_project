import pandas


class ColumnPairConverter(object):
    def convert_values_of_changeable_column_to_match_important_column(self, loaded_data: pandas.DataFrame,
                                                                      pair_important_column: str,
                                                                      pair_changeable_column: str)\
            -> pandas.DataFrame:
        pass