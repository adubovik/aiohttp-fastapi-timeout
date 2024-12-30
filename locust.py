from locust import HttpUser, constant_pacing, task

class User(HttpUser):
    wait_time = constant_pacing(1000000)

    @task
    def my_task(self):
        self.client.get("/")