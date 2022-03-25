import sys,pymongo

def list_all(uri: str):
    the_client = pymongo.MongoClient(uri)
    the_db = the_client
    return the_db

if __name__ == "__main__":
    args = sys.argv
    try:
        db_uri = args[1]
    except:
        raise ("Invalid Usage! Correct Usage: python3 main.py mongodb://example.com:27017/")
    else:
        print(list_all(db_uri))