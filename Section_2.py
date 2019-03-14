import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printVector(self):
        print("[%s, %d]" % (self.x, self.y))

    def length(self):
        return round(math.sqrt(pow(self.x, 2) + pow(self.y, 2)), 2)

    def slope(self):
        return round(self.y / self.x, 1)

    def normalVector(self):
        return True

    def azimuth(self):
        return True

    def angle(self, v):
        return True

    def sumVectors(self, v):
        return True


v1 = Vector(1, 3)
v1.printVector()
print("Length: ", v1.length())
print("Slope: ", v1.slope())
#nv = v1.normalVector()
#print("Normal vector: ", end = " ")
#nv.printVector()
#print("Azimuth: ", v1.azimuth())
#v2. = Vector(-3, 1)
#print("Angle between vectors: ", v2.angle(v1))
#v3 = v1.sumVectors(v2)
#print("Sum: ", end = " ")
#v3.printVector()
