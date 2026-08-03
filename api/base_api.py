
class BaseAPI:

    def __init__(self, api):
        self.api = api

    def get(self,endpoint):
        return self.api.get(endpoint)

    def post(self,endpoint,payload):
        return self.api.post(
            endpoint,
            data=payload
        )

    def put(self,endpoint,payload):
        return self.api.put(
            endpoint,
            data=payload
        )

    def delete(self,endpoint):
        return self.api.delete(endpoint)
