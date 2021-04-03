from nan_value_filler.classes.nan_filler.nan_filler import NanFiller


class FillWithMeanValue(NanFiller):
    def __init__(self):
        super().__init__()
        self.name = "fill_with_mean_value"

    def fill_nan_values(self, data_set_info, filling_column_name):
        mean_value = data_set_info.data_set[filling_column_name].mean()
        data_set_info.data_set[filling_column_name] = data_set_info.data_set[filling_column_name].fillna(mean_value)

        return data_set_info
