import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

# hash(md5)
import hashlib

# import housing class
from housing import Housing

# import queryUtils functions
import queryUtils
from queryUtils import getResult
from queryUtils import loginPost
from queryUtils import registerPost
from queryUtils import favoritePost
from queryUtils import favoriteGet
from queryUtils import favoriteRemove
from queryUtils import recommendation

import requests

#import DB
import pymongo
from pymongo import MongoClient


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # get the path of the request
        path = self.path
        print("path: " + str(path))

        # print out headers and the contet type
        print('Headers:"', self.headers, '"')
        print('Content-Type:', self.headers['content-type'])

        # get the length of the body
        length = int(self.headers['content-length'])
        # this is grabbing the info from Javascriptm reading the body
        body = self.rfile.read(length)

        # print body
        print('Body:', body)
        # convert bytes to string using .decode()
        print("Body (String): ", body.decode())

        # convert the body to a dictionary
        dictionary = json.loads(body)
        # To access a specific key from the dictionary:
        print("get the info from JS")
        print("dictionary : ")
        print(dictionary)
        # now we need to use this dictionary to make an Order class.

        if path == "/api/list":
            print("list!!")
            # Object Oriented for housing class
            tempDict = Housing(
                dictionary["zip"], dictionary["numOfHH"], dictionary["hHI"], dictionary["housingType"])

            housingList = queryUtils.getResult(tempDict.dictionary())
            res = json.dumps(str(housingList))

            self.send_response(200)
            self.end_headers()
            print(res)
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)

        elif path == "/api/housingAdd":
            if queryUtils.newHousing(dictionary)==True:
                print("housing registration is successful")
                self.send_response(200)
                self.end_headers()    
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/housingAdd")           

        # checking user info for login
        elif path == "/api/login":
            tempSalt = "SeniorProject"
            # hash the password and update the password
            tempHashPass = hashlib.md5(
                (dictionary["password"]+tempSalt).encode())
            # saving as hexadecimal value
            dictionary["password"] = tempHashPass.hexdigest()

            # check login info with userAccount DB
            if queryUtils.loginPost(dictionary) == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/login")

        # checking user info for registration
        elif path == "/api/register":
            tempSalt = "SeniorProject"
            tempHashPass = hashlib.md5(
                (dictionary["password"]+tempSalt).encode())
            dictionary["password"] = tempHashPass.hexdigest()

            if queryUtils.registerPost(dictionary) == True:
                print("user registration is successful")
                self.send_response(200)
                self.end_headers()

            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/register")

        # checking admin info for login
        elif path == "/api/adminLogin":
            tempSalt = "SeniorProject"
            # hash the password and update the password
            tempHashPass = hashlib.md5(
                (dictionary["password"]+tempSalt).encode())
            # saving as hexadecimal value
            dictionary["password"] = tempHashPass.hexdigest()

            # check login info with userAccount DB
            if queryUtils.adminLoginPost(dictionary) == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/login")

        # checking admin info for registration
        elif path == "/api/adminRegister":
            accessCodeAns = "COSC4362"
            tempSalt = "SeniorProject"
            tempHashPass = hashlib.md5(
                (dictionary["password"]+tempSalt).encode())
            dictionary["password"] = tempHashPass.hexdigest()

            if queryUtils.adminRegisterPost(dictionary) == True and dictionary["accesscode"] == accessCodeAns:
                print("user registration is successful")
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/adminRegister")                


        elif path == "/api/favorite":
            favorQueryResponse = queryUtils.favoritePost(dictionary)
            if favorQueryResponse == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/favorite")

        elif path == "/api/favoriteremove":
            favorQueryResponse = queryUtils.favoriteRemove(dictionary)
            if favorQueryResponse == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/favoriteremove")

        elif path =="/api/housingListRemove":
            housingListResponse =queryUtils.housingListRemove(dictionary)
            if housingListResponse == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/housingListRemove")

        elif path =="/api/userListRemove":
            userListResponse = queryUtils.userListRemove(dictionary)
            if userListResponse == True:
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(403)
                self.end_headers()
                print("there is error in /api/userListRemove")

        elif path == "/api/getfavorite":
            favoriteResponse = queryUtils.favoriteGet(dictionary)
            res = json.dumps(str(favoriteResponse))
            self.send_response(200)
            self.end_headers()
            print(res)
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)

        elif path == "/api/getHousingList":
            housingListQuery = queryUtils.getHousingList()
            res = json.dumps(str(housingListQuery))
            self.send_response(200)
            self.end_headers()
            print(res)
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)      

        elif path == "/api/getUseraccountList":
            userListQuery = queryUtils.getUserAccountList()
            res = json.dumps(str(userListQuery))
            self.send_response(200)
            self.end_headers()
            print(res)
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)   

        
        elif path == "/api/recommendation":
            reqResponse =  queryUtils.recommendation(dictionary)
            res = json.dumps(str(reqResponse))
            self.send_response(200)
            self.end_headers()
            print(res)
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)


        else:
            self.send_response(404)
            self.end_headers()


def main():
    # establishing the connection to our server
    port = 8000
    server_address = ('localhost', port)
    server = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Running on port", port)
    server.serve_forever()


# run main function
if __name__ == "__main__":
    main()
