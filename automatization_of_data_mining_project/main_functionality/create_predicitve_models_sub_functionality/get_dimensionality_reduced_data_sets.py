from typing import List

from data_set_dimension_reductioner import DimensionReducer
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.factor_analysis_dimension_reduction import \
    FactorAnalysisDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.low_variance_filter_dimension_reduction import \
    LowVarianceFilterDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.pca_dimension_reduction import PCADimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction.random_forest_dimension_reduction import \
    RandomForestDimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction_statistics_reporter.document_statistic_reporter import \
    DimensionReductionDocumentStatisticReporter
from data_set_info_data_class.data_class.preprocessed_data_set_info import PreprocessedDataSetInfo


def get_dimensionality_reduced_data_sets(preprocessed_data_set: PreprocessedDataSetInfo):
    # Here default parameters are used, we can instantiate multiple dimension reduction algorithms with different parameters
    low_variance_dimension_reduction = LowVarianceFilterDimensionReduction()
    random_forest_dimension_reduction = RandomForestDimensionReduction()
    pca_dimension_reduction = PCADimensionReduction()
    factor_analysis_dimension_reduction = FactorAnalysisDimensionReduction()

    statistic_reporter = DimensionReductionDocumentStatisticReporter(
        "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics/dimension_reduction_statistics")

    data_set_dimension_reductioner = DimensionReducer(
        dimension_reductioners=[low_variance_dimension_reduction,
                                random_forest_dimension_reduction,
                                pca_dimension_reduction,
                                factor_analysis_dimension_reduction],
        statistic_reporter=statistic_reporter
    )

    train_dimension_reduction_results: List[
        DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(preprocessed_data_set.x_train,
                                                                                         preprocessed_data_set.y_train)

    data_set_dimension_reductioner.create_dimension_reduction_statistics(train_dimension_reduction_results)

    test_dimension_reduction_results: List[
        DimensionReductionResult] = data_set_dimension_reductioner.get_reduced_data_sets(preprocessed_data_set.x_test,
                                                                                         preprocessed_data_set.y_test)

    return train_dimension_reduction_results, test_dimension_reduction_results


