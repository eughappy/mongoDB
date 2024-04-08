from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def delete_all(client:MongoClient):
    try:
        db = client.book
        for i in db.cats.find():
            db.cats.delete_one({"name": i['name']})
    except Exception as e:
        print(e)

def delete_one(client:MongoClient):
    name = str(input('Input name of cat that you want to delete: '))
    try:
        db = client.book
        db.cats.delete_one({"name": name})
    except Exception as e:
        print(e)

def read_one(client:MongoClient):
    name = str(input('Input name of cat that you want to see: '))
    try:
        db = client.book
        if db.cats.find_one({"name":name}) != None:
            print(db.cats.find_one({"name":name}))
        else:
            print('No such cat!')
    except Exception as e:
        print(e)

def read_all(client:MongoClient):
    temp = 1
    try:
        db = client.book
        for i in db.cats.find():
            print(f"It's {temp} cat:")
            temp += 1
            query = str(i).replace('{','')
            query = query.replace('}','')
            print(query,"\n")
    except Exception as e:
        print(e)

def update_age(client:MongoClient):
    try:
        name = str(input('Input name of cat that you want to change: '))
        age = int(input('Input age that you want to set for your cat: '))
    except Exception as e:
        print(e)
    try:
        db = client.book
        db.cats.update_one(
            {"_id":db.cats.find_one({"name":name})["_id"]},
            {
                "$set": {
                    "age":age
                }
            }
        )
    except Exception as e:
        print(e)

def update_features(client:MongoClient):
    try:
        name = str(input('Input name of your cat: '))
        features = str(input('Input features of cat with spaces: ')).split()
    except Exception as e:
        print(e)    
    try:
        db = client.book
        new_features = db.cats.find_one({"name":name})["features"]
        for i in features:
            new_features.append(i)
        db.cats.update_one(
            {"_id":db.cats.find_one({"name":name})["_id"]},
            {
                "$set": {
                    "features":new_features
                }
            }
        )
    except Exception as e:
        print(e)

def insert_cat(client:MongoClient):
    try:
        name = str(input('Input name of your cat: '))
        age = int(input('Input age that you want to set for your cat: '))
    except Exception as e:
        print(e)
    features = str(input('Input features of cat with spaces: ')).split()
    try:
        db = client.book
        db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features
        }
        )
    except Exception as e:
        print(e)

if __name__ == '__main__':
    uri = 'mongodb+srv://eughappy:mpUpOVC4NXeuF5Ky@pygoitdatabase.tlthamp.mongodb.net/'
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    while True:
        choice = str(input('''
Hello. What do you want to do with the database?
        1 - update_age
        2 - update_features
        3 - delete_one
        4 - delete_all
        5 - read_one
        6 - read_all  
        7 - insert_cat    
        0 - exit   
'''))
        if choice == '1':
            update_age(client)
        elif choice == '2':
            update_features(client)
        elif choice == '3':
            delete_one(client)
        elif choice == '4':
            delete_all(client)
        elif choice == '5':
            read_one(client)
        elif choice == '6':
            read_all(client)
        elif choice == '7':
            insert_cat(client)
        elif choice == '0':
            print('Thank you for using database!')
            break
        else:
            print("We are sorry, you input incorrect value!")
            


