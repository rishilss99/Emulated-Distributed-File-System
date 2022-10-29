from importlib.metadata import metadata
from pymongo import MongoClient
import pprint
import datetime

"""An important consideration when working with the file system functions of this EDFS
    is that they require absolute path much like the Hadoop DFS"""


class MongoMetadata:
    def __init__(self):
        # MongoDB database's connection string
        conn_str = "mongodb+srv://dsci551:dsci551@cluster0.eks9nfe.mongodb.net/test"
        client = MongoClient(conn_str)

        # Database
        db = client['EDFS_Directory']

        # Collection
        self.collection = db['DSCI551']

    def mkdir(self, path):

        if path[0] != '/':
            print("Require absolute path starting from root")
            return
        path_list = path.split("/")
        doc = self.collection.find({"root": {'$exists': 1}})
        head_itr = doc[0]['root']
        prev_val = head_itr
        for dir in path_list[1:]:
            if dir not in head_itr:
                head_itr[dir] = {}
            head_itr = head_itr[dir]
        self.collection.update_one({"root": {'$exists': 1}}, {
                                   "$set": {"root": prev_val}})

    def ls(self, path):

        if path[0] != '/':
            print("Require absolute path starting from root")
            return

    def cat(self, path):

        if path[0] != '/':
            print("Require absolute path starting from root")
            return

    def rmdir(self, path):

        if path[0] != '/':
            print("Require absolute path starting from root")
            return

    def rm(self, path):

        if path[0] != '/':
            print("Require absolute path starting from root")
            return


# post = {"root":{}}

metadata = MongoMetadata()
metadata.mkdir("/home/shreeram")

# print(post_id)
