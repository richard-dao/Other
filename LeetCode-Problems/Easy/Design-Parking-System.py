# Python
class ParkingSystem(object):
    b = 0
    m = 0
    s = 0

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.b = big
        self.m = medium
        self.s = small
        
    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if (carType == 1):
            if (self.b == 0):
                return False
            self.b = self.b-1
            return True
        if (carType == 2):
            if (self.m == 0):
                return False
            self.m = self.m-1
            return True
        if (carType == 3):
            if (self.s == 0):
                return False
            self.s = self.s-1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
