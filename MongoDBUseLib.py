from pymongo import MongoClient

class UseMongoDB():
    db = ""
    dbName = "dbName_in_mlab"
    dbCollectionName = "collectionName_in_mlab"
    
# Setup
    #Free MongoDB host mlab.com 500MB free
    # Init the DB and provide cursor
    def __init__(self):
        client = MongoClient()
        client = MongoClient('mongodb://username:password@mongoDBServer.com:portNumber/db_deployment_in_mlab')
        self.db = client['{}'.format(self.dbName)]#

    def getCursor(self):
        return self.db

###################################################################################
#Write Data

    #Write data in mongoDB
    def writeInDB(self, data):
        result = posts.insert_one(data)

###################################################################################
#Get DATA

    # Get all data
    def getAllData(self):
        try:
            dbResult = self.db['{}'.format(self.dbCollectionName)].find()
            dbResultList = []
            for emps in dbResult:
                #print emps
                dbResultList.append(emps)
        except Exception, e:
            print str(e)
        return dbResultList