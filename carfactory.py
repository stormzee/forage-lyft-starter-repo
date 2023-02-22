from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbinbattery import NubbinBattery
from battery.spindlerbattery import SpindlerBattery
from tyre.Carrigan_tyre import CarriganTyre
from tyre.Octoprime_tyre import OctoprimeTyre

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear_array):
       
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        tyre = CarriganTyre(tyre_wear_array)
        calliope = Car(engine, battery, tyre)
        
        return calliope
        
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear_array):
        
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        tyre = OctoprimeTyre(tyre_wear_array)
        glissade = Car(engine, battery, tyre)
            
        return glissade
    
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tyre_wear_array): 
    
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(last_service_date, warning_light_on)
        tyre = CarriganTyre(tyre_wear_array)
        palindrome = Car(engine, battery, tyre)
            
        return palindrome
    
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear_array):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        tyre = OctoprimeTyre(tyre_wear_array)
        rorschach = Car(engine, battery, tyre)
        
        return rorschach
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear_array):
        
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        tyre = OctoprimeTyre(tyre_wear_array)
        thovex = Car(engine, battery, tyre)   
        
        return thovex


        
        
        