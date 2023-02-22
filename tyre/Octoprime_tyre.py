from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear_array:list):
        self.tyre_wear_array = tyre_wear_array
        
        
    def needs_service(self):
        return sum(self.tyre_wear_array) >= 3
        
    