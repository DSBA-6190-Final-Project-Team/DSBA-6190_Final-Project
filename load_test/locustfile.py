  
from locust import Locust, HttpLocust, TaskSet, task, between

class MyTaskSet(TaskSet):
    @task(1)
    
    def index(self):
        self.client.get("/")
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 15)