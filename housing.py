#from enum import Enum

# class EnumNumofHH(Enum):
#     one = "1 Person HouseHold"

#class EnumHousingType(Enum):
#    ALL = 1
#    RESIDENTIAL_HOUSING = 2
#    STUDENT_HOUSING = 3
#    ACCESSIBLE_HOUSING = 4
#    SENIOR_HOUSING = 5
    
# Housing Type
# All, Accessible Housing, Children's Shelter, Residential Housing, Senior Housing, Student Housing, Transitional Housing

class Housing:
    def __init__(self,zip,numOfHH,hHI,housingType):
        self.zip = zip
        self.numOfHH = numOfHH
        self.hHI = hHI
        self.housingType = housingType
        #super().__init__()


    #getter and setter for zip
    def getZip(self):
        return self.getZip
    def setZip(self, tempZip):
        self.zip = tempZip

    #getter and setter for number Of Household
    def getNumOfHH(self):
        return self.numOfHH
    def setNumOfHH(self, tempNumOfHH):
        self.numOfHH = tempNumOfHH

    #getter and setter for Household Income
    def getHHI(self):
        return self.hHI
    def setHHI(self, tempHHI):
        self.hHI = tempHHI

    #getter and setter for Housing type
    def getHousingType(self):
        return self.housingType
    def setHousingType(self, tempHousingType):
        self.housingType = tempHousingType

    
    #make the dictionary function
    def dictionary(self):
        dict={
            'zip' : self.zip,
            'numOfHH' : self.numOfHH,
            'hHI' : self.hHI,
            'housingType' : self.housingType
        }
        return dict