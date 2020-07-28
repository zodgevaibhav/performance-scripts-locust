# 1. If any of task need to perform once and that too begining and after the TASK we can use these methods.

from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)

    @task
    def on_start(self):
        print("I am logging in to URL")

    @task
    def perform_transaction(self):
        print("I am performing task")


    @task
    def on_stop(self):
        print("I am logging out to URL")
