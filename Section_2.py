import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printVector(self):
        print("[%s %d]" % (self.x, self.y))

    def length(self):
        return round(math.sqrt(pow(self.x, 2) + pow(self.y, 2)), 2)

    def slope(self):
        if self.x > 0 and self.y > 0:
            return round(self.y / self.x, 1)
        else:
            return 0

    def normalVector(self):
        return Vector(self.y * -1, self.x)
        
    def azimuth(self):
        if self.x == 0 or self.y == 0:
            if self.x == 0 and self.y != 0:
                if self.y > 0:
                    return 90.0
                elif self.y < 0:
                    return 270.0
            elif self.x != 0 and self.y == 0:
                if self.x > 0:
                    return 0.0
                elif self.x < 0:
                    return 180.0
        else:
            if self.x > 0 and self.y >= 0:
                return round(math.degrees(math.atan(self.y / self.x)), 1)
            elif self.x < 0 and self.y > 0:
                return round(math.degrees(math.atan(self.y / abs(self.x))) + 90, 1)
            elif self.x < 0 and self.y < 0:
                return round(math.degrees(math.atan(self.y / self.x)) + 180, 1)
            elif self.x > 0 and self.y < 0:
                return round(math.degrees(math.atan(abs(self.y) / self.x)) + 270, 1)

    def angle(self, v):
        if v.azimuth() == self.azimuth():
            return  0.0
        elif v.azimuth() + 180 == self.azimuth() or v.azimuth() - 180 == self.azimuth():
            return 180.0
        else:
            return round(math.degrees(math.acos((self.x * v.x + self.y * v.y) / (self.length() * v.length()))), 1)

    def sumVectors(self, v):
        return Vector(self.x + v.x, self.y + v.y)


v1 = Vector(1, 3)
v1.printVector()
print("Length: ", v1.length())
print("Slope: ", v1.slope())
nv = v1.normalVector()
print("Normal vector: ", end = "")
nv.printVector()
print("Azimuth: ", v1.azimuth())
v2 = Vector(-3, 1)
print("Angle between vectors: ", v2.angle(v1))
v3 = v1.sumVectors(v2)
print("Sum: ", end = "")
v3.printVector()
