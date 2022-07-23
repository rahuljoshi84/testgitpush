import pymongo

client = pymongo.MongoClient("mongodb+srv://rahuljoshi84:Rahuljoshi@cluster0.fmka9vw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
