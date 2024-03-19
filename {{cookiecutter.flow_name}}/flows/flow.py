from prefect import task, Flow
from prefect.schedules import Schedule
from prefect.schedules.clocks import CronClock

@task
def task1():
    return "Result of Task 1"

@task
def task2(input):
    return f"Result of Task 2 with input {input}"

cron_expression = "{{ cookiecutter.cron_expression }}"  # Use the user-defined cron expression
schedule = Schedule(clocks=[CronClock(cron_expression)])

with Flow("{{ cookiecutter.flow_name }}", schedule=schedule) as flow:  # Use the user-defined flow name
    t1_result = task1()
    t2_result = task2(t1_result)

if __name__ == "__main__":
    flow.register(project_name="{{ cookiecutter.project_slug }}")  # Use the user-defined project name
