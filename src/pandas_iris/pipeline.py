
# This is a boilerplate pipeline
# generated using Kedro 0.18.1


from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_predictions, report_accuracy, split_data, make_scatter_plot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=make_scatter_plot,
                inputs="example_iris_data",
                outputs="iris_scatter_plot@matplotlib",
                name="scatter_plot",
            ),
            node(
                lambda x: x, # because there is no transformation, just encoding exercise
                inputs="iris_scatter_plot@bytes",
                outputs="iris_scatter_plot_base64",
                name="encoding",
            ),
            node(
                func=split_data,
                inputs=["example_iris_data", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split",
            ),
            node(
                func=make_predictions,
                inputs=["X_train", "X_test", "y_train"],
                outputs=["y_pred", "trained_model"],
                name="make_predictions",
            ),
            node(
                func=report_accuracy,
                inputs=["y_pred", "y_test"],
                outputs="accuracy",
                name="report_accuracy",
            ),
        ]
    )
