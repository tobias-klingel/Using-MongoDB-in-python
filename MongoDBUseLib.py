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

    # Add a key/value pair in a exsisting document of DB. Based on a primary key (specific value which just this entry has)
    def updatebyPrimKey(self, primKey, primValue, key, value):
        collection = self.db['{}'.format(self.dbCollectionName)]
        return collection.update_one({"{}".format(primKey): primValue}, {"$set": {"{}".format(key): "{}".format(value)}})

###################################################################################
#Get DATA

    # Get all data
    def getAllData(self):
        try:
            dbResult = self.db['{}'.format(self.dbCollectionName)].find()
            dbResultList = []
            for emps in dbResult:
                dbResultList.append(emps)
        except Exception, e:
            print str(e)
        return dbResultList

    #Get all data in DB which has a specific key value
    def getAllDataOfACertainKeyValue(self, key, value):
        return self.db['{}'.format(self.dbCollectionName)].find_one({"{}".format(key): "{}".format(value)})

    # Get all values in data base of a certain key
    def getAllEntriesOfCertainKey(self, key):
        allData = self.getAllData()
        allDataFilteredbyKey = []
        for i in range(len(allData)):
            allDataFilteredbyKey.append(self.extactOneField(allData[i], key))
        return allDataFilteredbyKey

###################################################################################
#Check methods

    #Check if certain key Value pair exist
    def checkIfKeyValueExist(self, key ,value):
        existence = self.db['{}'.format(self.dbCollectionName)].find_one({"{}".format(key):"{}".format(value)})
        if (existence != None):
            return True
        else:
            return False
