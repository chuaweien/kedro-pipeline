# Pandas Iris

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.1`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## Kedro with KubeFlow Pipeline
### Package Kedro pipelines into Docker
First, you will need to install `kedro-docker` to help you generate the `Dockerfile` for your Kedro Pipeline.
```
pip install kedro-docker
```
After installing the plugin, navigate to your project root folder and run the following command to generate `Dockerfile`, `.dockerignore` and `.dive-ci` files.
```
kedro docker init
```
Then, build the project image using the `Dockerfile` that was generated using the below command.
```
kedro docker build
```
Once the project image has been built, you can run the project image with the following command or you can push the docker image into your Docker Registry for for KubeFlow Pipeline.
```
kedro docker run
```

### Generate Workflow Specs
Using the workflow specs `build_kubeflow_pipeline.py` referenced from Kedro Documentation, it will generate `Pandas Iris.yaml` file to upload to KubeFlow Pipeline. The python script can be run with the command below at the project root directory.
```
python build_kubeflow_pipeline.py
```

## Kedro with MLFlow
> Note: MLFlow plugin is compatible with `kedro>=0.16.0`

To use MLFlow with Kedro, you will need to install the plugin.
```
pip install kedro-mlflow
```
After installing, initiate the plugin by running:
```
kedro mlflow init
```
The initiation is successful if `mlflow.yml` file is generated in `conf/local` folder with the following message:
```
'conf/local/mlflow.yml' successfully updated.
```
Once you have initiate the plugin, the first time you run a `kedro run` a new `mlruns` folder will be created with all the experiment trackings and artifacts if you left the MLFlow tracking uri as default (i.e. local server).

You can specify the tracking uri to your own MLFlow server in the `mlflow.yml`.
## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
