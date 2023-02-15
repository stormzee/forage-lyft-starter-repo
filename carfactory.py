from abc import ABC, staticmethod 
from car import Car
from datetime import datetime
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from nubbinbattery import NubbinBattery
from spindlerbattery import SpindlerBattery



class CarFactory:
    
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
       
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        calliope = Car(engine, battery)
        
        return calliope
        
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        glissage = Car(engine, battery)
            
        return glissade
    
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool): 
    
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        palindrome = Car(engine, battery)
            
        return palinndrome
    
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        rorschach = Car(engine, battery)
        
        return rorschach
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        thovex = Car(engine, battery)   
        
        return thovex


        
        
        