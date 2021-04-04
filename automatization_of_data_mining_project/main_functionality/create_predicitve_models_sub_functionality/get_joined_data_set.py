from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_joiner import Joiner
from datetime import datetime

import csv
import os


def get_joined_data_set(data_sets_info: List[DataSetInfo]):
    data_set_joiner = Joiner()

    all_data_frames = []

    for data_set_info in data_sets_info:
        all_data_frames.append(data_set_info.data_set)

    join_by_columns = ['Year', 'Country Code']

    joined_data_frame = data_set_joiner.join_data_sets(all_data_frames, join_by_columns)

    # save joined data frame
    path = "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/joined_data_sets"
    current_time = datetime.now()
    current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
    filename = os.path.join(
        path + "/joined_data_set_" + current_time_string + ".csv")
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(joined_data_frame.values)

    return joined_data_frame
