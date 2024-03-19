from prefect import task, Flow
from prefect.schedules import Schedule
from prefect.schedules.clocks import CronClock

@task
def task1():
    """
    Run task #1
    """
    return "Result of Task 1"

@task
def task2(input):
    """
    Run task #2
    """
    return f"Result of Task 2 with input {input}"

cron_expression = "{{ cookiecutter.cron_expression }}"  # Use the user-defined cron expression from cookiecutter parameters
schedule = Schedule(clocks=[CronClock(cron_expression)])  # Create a Schedule object from the cron expression

with Flow("{{ cookiecutter.flow_name }}", schedule=schedule) as flow:  # Setup a Flow object and assign tasks
    t1_result = task1()
    t2_result = task2(t1_result)

if __name__ == "__main__":
    flow.register(project_name="{{ cookiecutter.project_name }}")  # Register flow with Prefect server
