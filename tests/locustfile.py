
from locust import HttpUser, task, between

class AveragePageUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/auth/login", data={"username": "admin", "password": "admin123"})

    @task
    def view_averages(self):
        self.client.get("/notes/averages")
