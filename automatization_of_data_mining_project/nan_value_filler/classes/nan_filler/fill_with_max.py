from nan_value_filler.classes.nan_filler.nan_filler import NanFiller


class FillWithMaxValue(NanFiller):
    def __init__(self):
        super().__init__()
        self.name = "fill_with_max_value"

    def fill_nan_values(self, data_set_info, filling_column_name):
        max_value = data_set_info.data_set[filling_column_name].max()
        data_set_info.data_set[filling_column_name] = data_set_info.data_set[filling_column_name].fillna(max_value)

        return data_set_info
