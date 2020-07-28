from locust import User,task,between,constant,constant_pacing


class MyUser(User):
    wait_time = between(1,2) #It is wait time betweek two iteration/task. Even if it is single use this property is mandatory
#    wait_time = constant(1) #it will wait 1 second after every task execution
#    wait_time = constant_pacing(1) #it will run next task every 1 seconds irrespective of how much time current task takes


    @task
    def login_URL(self):
        print("I am logging in to URL")
