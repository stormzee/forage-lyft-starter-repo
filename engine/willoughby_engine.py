from engine.engine import Engine
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class WilloughbyEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
