import socket

class HealthcheckService():
    def __init__(self):
        pass

    def check(self):
        return {
            "status": "up",
            "hostname": socket.gethostname(),
        }