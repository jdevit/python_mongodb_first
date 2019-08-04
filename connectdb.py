import pymongo
import mongoengine
import datetime
# import os
# print(os.listdir())
# from urllib.request import urlopen
# print(urlopen('https://www.howsmyssl.com/a/check').read())



def jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied):
	job = {"_id": numDocs + 1, "role_title": role_title, "company": company, "location": location, "platform": platform,
		   "cover_letter": cover_letter, "date_applied": date_applied, "published": datetime.datetime.now()}
	return job


def openTextfile(filename):
	file = open(filename, 'r')
	contents = file.read()
	contents = contents.split(",")
	return contents


def connectToDb():
	usernamepasswordFile = "userpass.txt"
	usernamepassword = openTextfile(usernamepasswordFile)
	username = usernamepassword[0]
	password = usernamepassword[1]

	## Estalishing connection ##
	## Azure
	host = "mongodb+srv://" + username + ":" + password + "@clusterj-zlrbh.azure.mongodb.net/test?retryWrites=true&w=majority"
	## MongoEngine
	mongoengine.connect('mongoengine_test', host=host)
	client = pymongo.MongoClient(host)
	return client

def getCollection(client):
	db = client.newdb
	return db.jobapplications

def saveToDb(collection, role_title, company, location, platform, cover_letter, date_applied):
	# # Inserting Documents ##
	numDocs = len(list(collection.find()))

	job = jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied)
	print(job)
	collection.insert(job)


def main():
	print("Heloo")

	client = connectToDb()
	col = getCollection(client)

	saveToDb(col)

	print("End.")

if __name__ == "__main__":
	main()
