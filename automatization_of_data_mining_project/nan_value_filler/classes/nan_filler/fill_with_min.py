from nan_value_filler.classes.nan_filler.nan_filler import NanFiller


class FillWithMinValue(NanFiller):
    def __init__(self):
        super().__init__()
        self.name = "fill_with_min_value"

    def fill_nan_values(self, data_set_info, filling_column_name):
        min_value = data_set_info.data_set[filling_column_name].min()
        data_set_info.data_set[filling_column_name] = data_set_info.data_set[filling_column_name].fillna(min_value)

        return data_set_info
