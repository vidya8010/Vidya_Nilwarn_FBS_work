# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Destructor called")

    def __add__(self, d):
        cm = self.cm + d.cm
        m = self.m + d.m
        km = self.km + d.km

        if cm >= 100:
            cm = cm - 100
            m = m + 1

        if m >= 1000:
            m = m - 1000
            km = km + 1

        return Distance(km, m, cm)

    def __sub__(self, d):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = d.km * 100000 + d.m * 100 + d.cm

        difference = total1 - total2

        km = difference // 100000
        difference = difference % 100000

        m = difference // 100
        cm = difference % 100

        return Distance(km, m, cm)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")


d1 = Distance(5, 800, 75)
d2 = Distance(2, 500, 50)

d3 = d1 + d2
d4 = d1 - d2

print("Addition:")
d3.display()

print("Subtraction:")
d4.display()