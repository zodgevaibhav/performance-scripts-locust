#1. How to get current time of machine
#2. How to print time. How to convert datetime to String
#3. how to concatinate the strings
#4. Verify time by using constant and constant_pacing wait_time properties

from locust import User,task,between#,constant, constant_pacing
from datetime import  datetime


class MyUser(User):
    wait_time = between(1,4)

    #wait_time = constant(4)
    #wait_time = constant_pacing(1)

    @task
    def login_URL(self):
        print("I am logging in to URL" + str(datetime.now()))
