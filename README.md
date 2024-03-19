# Prefect Flow Cookiecutter Template

This repository contains a Cookiecutter template for creating Prefect flows, designed to help you kickstart your data workflow projects using Prefect for orchestration.

## Requirements

Before starting, make sure you have the following installed:
- Python 3.7+
- Cookiecutter Python package: `pip install cookiecutter`
- Prefect: `pip install "prefect<2"`

## Usage

1. Run the following command to generate a new Prefect flow project:
```
cookiecutter https://github.com/idon14/prefect-flow-template.git
```

2. You will be prompted to enter:
- `project_name`: Your project name in Prefect server (e.g., `my_prefect_project`).
- `flow_name`: The name of your Prefect flow (e.g., `data_processing_flow`).
- `cron_expression`: A cron expression to schedule your flow (e.g., `"0 9 * * *"` for every day at 9 AM).

3. Once the project is created, navigate into your project directory:
```
cd <project_name>
```

4. Set up a virtual environment and install the required packages:
```
python -m venv venv
source bin/venv/activate
pip install -r requirements.txt
```

5. Develop your Prefect flow within the generated Python files.

6. To register your flow with Prefect Server, follow the configured CI/CD pipeline in your GitLab repository or manually register your flow:
```
python flows/flow.py
```

## Configuration

- `.gitlab-ci.yml` is configured to register the flow with Prefect upon pushing to the main branch. Customize it as needed.
- Modify the flow and deployment files as necessary to fit your workflow requirements.

To use GitLab CI pipeline, ensure that you have set your Prefect Server URL as environment variable in your GitLab project:

1. Go to your GitLab project.
2. Navigate to Settings > CI / CD and expand the Variables section.
3. Add your Prefect Server URL as PREFECT_SERVER_URL.

For more information on working with Prefect and developing flows, visit the [Prefect documentation](https://docs.prefect.io/).
