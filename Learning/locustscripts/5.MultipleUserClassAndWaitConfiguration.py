# 1. How to crate multiple use class
# 2. Behaviors if we execute script without UserClass name
#   ex. locust -f 5.MultipleUserClassAndWaitConfiguration.py
#        - If 1 user selected then any one class will be exeuted
#        - If 2 users selected while execution then any of two user class will be picked
# 2.1 Locust by default span equal number of User class as per no. of Users mentioned while execution
#        - If 6 users selected while execution then all 3 classes will have 2 users spawn
# 3. How can we specifically ask which user to execute
#   ex. locust -f 5.MultipleUserClassAndWaitConfiguration.py WebUser
# 4. How can to add weigh to user classes and how locust create more thread of UserClass who has more weight


from locust import User,task,between


class WebUser(User):
    wait_time = between(1,2)
    weight = 1

    @task
    def login_URL(self):
        print("I am logging in to Web URL")


class MobileUser(User):
    wait_time = between(1, 2)
    weight = 2
    @task
    def login_URL(self):
        print("I am logging in to Mobile URL")


class APIUser(User):
    wait_time = between(1, 2)
    weight = 3
    @task
    def login_URL(self):
        print("I am logging in to API URL")