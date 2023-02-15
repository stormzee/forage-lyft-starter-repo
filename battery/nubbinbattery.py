import os
import sys
import datetime
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from battery.battery import Battery

class NubbinBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

    
    
        