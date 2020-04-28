from locust import HttpLocust, TaskSet, task, between
import os
import logging

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

host_url = "https://96gfw8ry96.execute-api.us-east-1.amazonaws.com"

post_path='Test/predict'

#headers = {
#    "Content-Type": "image/jpg"
#}

payload_path = "payload_files/img_1.jpg"

payload = open(payload_path, "rb").read()

class BaseTaskSet(TaskSet):
    
    def on_start(self):
        # Called everytime when a simulated user starts executing TaskSet class
        self.headers = {
            'content-type': "image/jpg"
        }
        
        LOG.info('Headers: {}'.format(self.headers))


class UserBehavior(BaseTaskSet):
    @task(1)
    def post_test(self):
        response = self.client.post(url=os.path.join(host_url, post_path),
                         data=payload,
                         headers = self.headers
        )

        LOG.info("Return Payload Status: {}".format(response))

class WebsiteUser(HttpLocust):
    host=host_url
    task_set=UserBehavior
    wait_time=between(5.0, 15)
