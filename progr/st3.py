import json
import pprint
import functools
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-name", help="person's name")
parser.add_argument("-surname", help="person's surname")
parser.add_argument("-m_name", help="person's middle name")
parser.add_argument("-m_phone", help="person's mobile phone", type=str)
parser.add_argument("-h_phone", help="person's home phone", type=str)
args = parser.parse_args()

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

class Storage:
    def __init__(self, db_name):
        self.db_name = db_name

    def _update_dict(tmp_dict):
        tmp_dict[k+1] = {"name":args.name, "surname":args.surname,"middle_name":args.m_name,"mobile_phone":args.m_phone, "home_phone":args.h_phone}
        return tmp_dict

    @to_json
    def read(self):
        storage_path = self.db_name
        if not os.path.isfile(storage_path):
            person = {}
            _update_dict(person)
            return person
        else:
            person = {}
            with open(storage_path, 'r') as f:
                raw_data = f.read()
                if raw_data:
                    person = json.loads(raw_data)
            return person        

    @to_json
    def write(self):
        storage_path = self.db_name  
        tmp = Storage(storage_path)
        new = json.loads(tmp.read())
        new[str(len(new)+1)] = {"home_phone": args.h_phone, "middle_name": args.m_name, "mobile_phone":args.m_phone, "name": args.name, "surname":args.surname}
        with open(storage_path, 'w') as f:
            json.dump(new, f)
        return new

    def _find(self,storage_path):
        pass
        
aa = Storage("/Users/utah/hw_univer/progr2/db.json")
tmp = aa.write()
pprint.pprint(tmp)