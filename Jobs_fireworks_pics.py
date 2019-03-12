from class_pics import Firewors
import sqlite3

def connect_db(db=None):
    cx = False
    cu = False
    if not db == None:
        cx = sqlite3.connect(db)
        cu = cx.cursor()
    return cx,cu


db = 'leyan.db'
d2 = r'files\\'

cx,cu = connect_db(db)
process_lofter_pics(url)
cx.close()




