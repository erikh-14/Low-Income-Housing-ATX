import queryUtils
from queryUtils import getResult
from pprint import pprint # for pretty print
#import housing class
from housing import Housing

#testing variables#
zip = 78702
HHI = 45000
NumOfHH = '2 Person Household'
HousingType = 'Residential Housing'

#testing Senior Housing list 
zip2 = 78754
HHI2 = 40000
NumOfHH2 = '2 Person Household'
HousingType2 = 'Senior Housing'


Dict = {}
Dict = dict({'zip': zip, 'hHI': HHI, 'numOfHH' : NumOfHH, 'housingType' : HousingType})

Dict2 = {}
Dict2 = dict({'zip': zip2, 'hHI': HHI2, 'numOfHH' : NumOfHH2, 'housingType' : HousingType2})

Dict2 = Housing(Dict2['zip'],Dict2['numOfHH'],Dict2['hHI'], Dict2['housingType'])


TemphousingList = queryUtils.getResult(Dict2.dictionary())
for count in TemphousingList:
    pprint(count)
    






#local machine with csv file
#import csv
#with open('Affordable_Housing_Listing.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        if(row['Zip Code'] == zip and row[NumOfHH] >= HHI):
#            print(row)    

