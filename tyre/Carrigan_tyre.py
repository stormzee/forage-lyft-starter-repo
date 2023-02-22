from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, tyre_wear_array:list):
        self.tyre_wear_array = tyre_wear_array
        
        
    def needs_service(self):
        greater_array = [i for i in self.tyre_wear_array if i > 0.9]
        return len(greater_array) >= 1
    