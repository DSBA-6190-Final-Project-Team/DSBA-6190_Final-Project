  
from locust import HttpLocust, TaskSet, task, between
import os

header = {
    "Content-Type" : "image/jpg"
}

payload_path = "payload_files/img_1.jpg"

payload = open(payload_path, "rb").read()

class UserBehavior(TaskSet):
    @task(1)
    def post_tests(self):
        self.client.post(path = "/Test/predict", 
                         data = payload, 
                         headers = header)
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 15)