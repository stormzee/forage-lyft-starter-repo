from engine.engine import Engine
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
