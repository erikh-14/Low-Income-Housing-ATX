import pymongo
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
# This python file has all query helper methods.

client = MongoClient()
# making a connection to a mongodb by using MongoClient with localhost url
url = 'mongodb://127.0.0.1:27017'
client = MongoClient(url)

# getting Affordable housing list
db = client.ahListing


def getResult(dict):
  # coonect to housing list table
    collection = db.ahListing
    houses = collection.find(
        {"Zip Code": dict['zip'], "Housing Type": dict['housingType'], dict['numOfHH']: {'$gte': dict['hHI']}})
    return list(houses)


# login helper method with user info
# dictionary is userinfo parameter, ex) username and password
# if username and password is matching with users database info then return userID. If it is not exist, then return None
def loginPost(dict):
    # connect to user account DB
    collection = db.userAccount
    user = collection.find_one(
        {"username": dict['username'], "password": dict['password']})

    if user != None:
        return True
    else:
        return False

# login helper method with admin info
# dictionary is userinfo parameter, ex) username and password
# if username and password is matching with admin database info then return userID. If it is not exist, then return None
def adminLoginPost(dict):
    # connect to user account DB
    collection = db.adminAccount
    user = collection.find_one(
        {"username": dict['username'], "password": dict['password']})

    if user != None:
        return True
    else:
        return False

# register helper function with user info
# dictionary includes username, password, first name, last name, email, and phone number.
# if there is no same username, then insert new user info data from dictionary and return true.
# However, if username is exist, then return False;


def registerPost(dict):
    # connect to user account DB
    collection = db.userAccount
    registerUser = collection.find_one({"username": dict['username']})

    if registerUser == None:
        collection.insert_one(dict)
        db.favorites.insert_one(
            {"username": dict['username'], "favoriteId": ""})
        return True
    else:
        return False

# register helper function with admin info
# dictionary includes username, password, first name, last name, email, and phone number.
# if there is no same username, then insert new admin info data from dictionary and return true.
# However, if username is exist, then return False;


def adminRegisterPost(dict):
    # connect to user account DB
    collection = db.adminAccount
    registerUser = collection.find_one({"username": dict['username']})

    if registerUser == None:
        collection.insert_one(dict)
        return True
    else:
        return False

def newHousing(dict):
    collection = db.ahListing
    addHousing = collection.find_one({"Address": dict['Address']})

    if addHousing == None:
        collection.insert_one(dict)
        return True
    else:
        return False


def favoriteRemove(dict):
    collection = db.favorites
    # print(dict)
    userFavorite = collection.find_one_and_update({"username": dict['username']}, {
                                                  '$set': {"favoriteId": dict['favoriteId']}})

    if userFavorite == None:
        return False
    else:
        return True

def housingListRemove(dict):
    collection = db.ahListing
    id=""
  
    for char in dict["housingId"]:
        if(char == " "):
            oid = ObjectId(id)
            collection.delete_one({'_id':oid})
            id =""
        else:
            id += char

    return True

def userListRemove(dict):
    collection = db.userAccount
    id = ""
    for char in dict["userId"]:
        if(char == " "):
            oid = ObjectId(id)
            collection.delete_one({'_id':oid})
            id =""
        else:
            id += char

    return True



def favoritePost(dict):
    collection = db.favorites

    existFavorite = collection.find_one({"username": dict['username']})
    newFavoriteIds = existFavorite.get("favoriteId") + dict['favoriteId']
    newFavorite = collection.find_one_and_update({"username": dict['username']}, {
                                                 '$set': {"favoriteId": newFavoriteIds}})

    if newFavorite == None:
        return False
    else:
        return True


def favoriteGet(dict):
    collection = db.favorites
    favoritelist = collection.find_one({"username": dict['username']})

    print("--favoriteGet---")
    print(type(favoritelist))
    print(favoritelist)

    housingList = favoritelist.get("favoriteId")
    print(housingList)
    print(type(housingList))
    # housingList = housingList[0:-1]
    print("count of space: ")
    print(housingList.count(' '))

    id = ""
    housingArray = []
    for char in housingList:
        if(char == " "):
            oid = ObjectId(id)
            house = db.ahListing.find_one(oid)
            housingArray.append(house)
            id = ""

        else:
            id += char

    return housingArray

def getHousingList():
    collection = db.ahListing
    housingList = collection.find()

    return list(housingList)

def getUserAccountList():
    collection = db.userAccount
    userAccountList = collection.find()

    return list(userAccountList)



def recommendation(dict):

    favoriteList = favoriteGet(dict)

    if(len(favoriteList) != 0):
        firstFavorite = favoriteList[0]
        print("--firstFavorite: --")
        print(firstFavorite)
        print(firstFavorite['Unit Type'])
        print(firstFavorite['2 Person Household'])

        # tempResults0 = db.ahListing.find({'Unit Type':"Single Family",'2 Person Household':41280}).limit(10)
        tempResults = db.ahListing.find({'Unit Type': firstFavorite['Unit Type'], '2 Person Household': firstFavorite['2 Person Household']}).limit(10)
    else:
        tempResults = ""

    return list(tempResults)
