# 1. If any of task need to perform once and that too begining and after the User/Test we can use these methods.
# 2. We need to use listeners in this case. Functions should be written in module leve
# 3. How to ad events in class
# Note :
#    Fired when a new load test is started. It's not fired again if the number of
#    users change during a test. When running locust distributed the event is only fired
#    on the master node and not on each worker node.



from locust import User,task,between,events

@events.test_start.add_listener
def test_start(**kwargs):
    print("********************** Before Test Start")

@events.test_stop.add_listener
def test_stop(**kwargs):
    print("********************** After Test Stop")


class MyUser(User):
    wait_time = between(1,2)

    @task
    def on_start(self):
        print("I am logging in to URL")

    @task
    def perform_transaction(self):
        print("I am performing task")


    @task
    def on_stop(self):
        print("I am logging out to URL")
