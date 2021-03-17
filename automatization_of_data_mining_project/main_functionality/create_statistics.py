from typing import List

from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_statistic_reporter import StatisticReporter
from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.classes.statistic_generator.implementations.column_names_statistic_generator import \
    ColumnNamesStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.missing_data_statistic_generator import \
    MissingDataStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.range_statistic_generator import \
    RangeStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.unique_impression_statistic_generator import \
    UniqueImpressionStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.variance_statistic_generator import \
    VarianceStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator
from data_set_statistic_reporter.classes.statistics_printer.document_statistics_printer import DocumentStatisticsPrinter
from data_set_statistic_reporter.classes.statistics_printer.statistics_printer import StatisticsPrinter
from data_set_statistic_reporter.exceptions.reporter_exceptions import WrongInputFormatError, NonIterableObjectError

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1
SUCCESS_STRING = colored('SUCCESS', 'green')


def create_data_sets_statistics_document(loaded_data_sets: List[DataSetInfo], document_path):
    statistics_printer: StatisticsPrinter = DocumentStatisticsPrinter(document_path)

    statistic_reporter = StatisticReporter(statistics_printer=statistics_printer)
    data_sets_as_statistic_reporter_data = create_statistic_reporter_data(loaded_data_sets)
    try:
        statistic_reporter.print_statistic(data_sets_as_statistic_reporter_data)
        print(SUCCESS_STRING,
              "Statistic document is created! It is located on 'generated_statistics' folder")
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for statistics data set reporter is invalid!\n")
        return
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for statistics data set reporter is not iterable!\n")
        return


def create_statistic_reporter_data(loaded_data_sets):
    data_sets_as_statistic_reporter_data: List[StatisticReporterDataClass] = []
    shared_statistic_generators = create_shared_statistic_generators()

    for data_set_info in loaded_data_sets:
        data_set_as_statistic_reporter_data = create_statistic_reporter_data_class(data_set_info,
                                                                                   shared_statistic_generators)
        data_sets_as_statistic_reporter_data.append(data_set_as_statistic_reporter_data)

    return data_sets_as_statistic_reporter_data


def create_shared_statistic_generators():
    columns_statistic_generator = ColumnNamesStatisticGenerator([])
    range_statistic_generator = RangeStatisticGenerator(['Year'])
    unique_impression_statistic_generator = UniqueImpressionStatisticGenerator(['Country Code'])
    variance_statistic_generator = VarianceStatisticGenerator(["Year"])
    shared_statistic_generators: List[StatisticGenerator] = [columns_statistic_generator,
                                                             range_statistic_generator,
                                                             unique_impression_statistic_generator,
                                                             variance_statistic_generator]
    return shared_statistic_generators


def create_statistic_reporter_data_class(data_set_info, shared_statistic_generators):
    missing_data_statistic_generator: StatisticGenerator = MissingDataStatisticGenerator(
        data_set_info.other_column_names)
    data_set_statistic_generators = shared_statistic_generators[:]
    data_set_statistic_generators.append(missing_data_statistic_generator)
    data_set_as_statistic_reporter_data = StatisticReporterDataClass(data_set_info.data_set_name,
                                                                     data_set_info.data_set,
                                                                     data_set_statistic_generators)
    return data_set_as_statistic_reporter_data
