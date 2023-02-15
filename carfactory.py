from abc import ABC, staticmethod 
from car import Car
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbinbattery import NubbinBattery
from battery.spindlerbattery import SpindlerBattery



class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
       
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        calliope = Car(engine, battery)
        
        return calliope
        
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        glissage = Car(engine, battery)
            
        return glissade
    
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on): 
    
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        palindrome = Car(engine, battery)
            
        return palinndrome
    
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        rorschach = Car(engine, battery)
        
        return rorschach
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        thovex = Car(engine, battery)   
        
        return thovex


        
        
        