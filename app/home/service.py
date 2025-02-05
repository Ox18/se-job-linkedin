from main.config import DEBUG
from main.utils.routes import getRoutes

class HomeService():    
    def main(self):

        if DEBUG:
            routes = getRoutes()
            return routes

        return {
            "message": "The service is running"
        }