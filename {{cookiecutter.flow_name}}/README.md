# {{cookiecutter.project_name}}

This project was generated with the Prefect Flow Cookiecutter template. It contains the initial setup for a Prefect flow, which you can now develop and extend according to your needs.

## Project Structure

- `flows/`: This directory contains your Prefect flow scripts.
- `.gitlab-ci.yml`: This file contains the CI/CD pipeline configuration for registering your flow with Prefect.

## Getting Started

1. Ensure you have Prefect installed, or install it via `pip install -v requirements.txt`.

2. Develop your flow in `flows/flow.py`. You can add new tasks, modify existing ones, and change the flow's schedule.

3. Test your flow locally by running:
```
python flows/flow.py
```

4. To register your flow with Prefect, ensure your Prefect Server is accessible and use:
```
python flows/flow.py
```

Make sure your Prefect environment is properly set up, including authentication and workspace selection.

## Deployment

The project is set up to use GitLab CI/CD for deploying your Prefect flow. Make sure to configure your Prefect Server URL as an environment variable in your GitLab project settings.
