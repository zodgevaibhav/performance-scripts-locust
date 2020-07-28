# 1. How to use HttpUser in the script. What all changes needed from last script
# 2. What are the mandatory parameters (host)
# 3. ways to give host parameter. (in script, in command line and while running test form UI

from locust import HttpUser,task,between


class MyUser(HttpUser):
    wait_time = between(1,2)  #Mandatory parameter
    host = "http://localhost:8081/customer/SearchCustomer/VVZ001"  #Mandatory parameter
    # Host can also be provided in command line. locust -f 2.HttpLocustScript.py

    @task
    def login_URL(self):
        print("I am logging in to URL")
