class Measurement:
    # *** add code here
    def __init__(self, label="undefined", feet=0, inches=0):
        self.label = label
        self.feet = feet
        self.inches = inches
    
    def set_label(self, label):
        self.label = label
    def set_feet(self, feet):
        self.feet = feet
    def set_inches(self, inches):
        self.inches = inches
    def getMeasurementString(self):
        
        
        return "{}' {}\"".format(self.feet, self.inches)

    def __str__(self):
        
        return "{}: {}".format(self.label, self.getMeasurementString())

    def addInches(self, amount):
        self.inches = self.inches + amount
        while self.inches >= 12:
            self.inches = self.inches - 12
            self.feet = self.feet + 1

    def getTotalInches(self):
        return (self.feet * 12) + self.inches

    def getCentimeters(self):
        return self.getTotalInches() * 2.54

    def getMetricString(self):
        cms = self.getCentimeters()
        return format(cms, ".2f") + " cm"


    
if __name__ == "__main__":

    
    office = Measurement()
    
    print(office.label)
    print(office.feet)
    print(office.inches)
    print()
    
    office.set_label("SH 186")
    office.set_feet(15)
    office.set_inches(3)
    print(office.label)
    print(office.feet)
    print(office.inches)
    print()
    
    alice = Measurement("Center Alice #16", 5,9)
    print(alice.label)
    print(alice.feet)
    print(alice.inches)
    print()
    
    print(alice)
    print()
    
    print(alice.getMeasurementString())
    print()
    
    alice.addInches(3)
    print(alice.getMeasurementString())
    print()
    
    print(alice.getTotalInches())
    print()
    
    print(alice.getCentimeters())
    print()
    
    print(alice.getMetricString())
    print()
    