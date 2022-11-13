from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("http://127.0.0.1:5000/home/0/3.14")
    
