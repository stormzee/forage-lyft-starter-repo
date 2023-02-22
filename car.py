from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre
        

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service()
