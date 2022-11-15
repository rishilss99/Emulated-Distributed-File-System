from importlib.metadata import metadata
from pymongo import MongoClient

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
            return "Require absolute path starting from root"
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
        return ["Success"]

    def ls(self, path):

        if path[0] != '/':
            return "Require absolute path starting from root"
        path_list = path.split("/")
        doc = self.collection.find({"root": {'$exists': 1}})
        head_itr = doc[0]['root']
        if path_list[-1] == '':
            return list(head_itr.keys())
        else:
            for dir in path_list[1:]:
                if dir not in head_itr:
                    return "Invalid path"
                head_itr = head_itr[dir]
            return list(head_itr.keys())

    def cat(self, path):

        if path[0] != '/':
            return "Require absolute path starting from root"
        path_list = path.split("/")
        if path_list[-1][-3:] != "csv":
            return "Invalid file type: Only .csv files allowed"
        doc = self.collection.find({"root": {'$exists': 1}})
        head_itr = doc[0]['root']
        for dir in path_list[1:-1:1]:
            if dir not in head_itr:
                return "Invalid file path"
            head_itr = head_itr[dir]
        if path_list[-1] not in head_itr.keys():
            return "File does not exist"
        else:
            f = open(path_list[-1])
            return list(f.read())

    def rm(self, path):

        if path[0] != '/':
            return "Require absolute path starting from root"
        path_list = path.split("/")
        doc = self.collection.find({"root": {'$exists': 1}})
        head_itr = doc[0]['root']
        prev_val = head_itr
        for dir in path_list[1:-1:1]:
            if dir not in head_itr:
                return "Invalid path"
            head_itr = head_itr[dir]
        if path_list[-1] not in head_itr.keys():
            return "File does not exist"
        else:
            del head_itr[path_list[-1]]
            self.collection.update_one({"root": {'$exists': 1}}, {
                "$set": {"root": prev_val}})
            return ["Success"]


# post = {"root":{}}
metadata = MongoMetadata()
a = metadata.rm("/home/ramu")
print(a)
# print(post_id)
