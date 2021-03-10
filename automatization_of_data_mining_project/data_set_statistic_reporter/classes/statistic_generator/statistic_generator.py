class StatisticGenerator(object):
    def __init__(self, column_names):
        self.column_names = column_names

    '''
        Function which returns two arrays:
            1. Statistic column names
            2. Statistic column values for each column name
    '''
    def generate_statistic(self, data_set) -> ([], []):
        pass