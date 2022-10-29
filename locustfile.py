from locust import HttpUser, task
            
class User(HttpUser):
    @task
    def get_home_route(self):
        self.client.get('/')
    @task
    def post_prediction(self):
        self.client.post('/predict',json={
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
})
