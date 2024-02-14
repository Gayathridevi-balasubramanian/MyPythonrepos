# Pickling 
# - Serializes the pyhton object and converts it into
#   the byte stream - dump
# Unpickling
# - deserislizes the byte stream and converts it into 
# the python object - 
import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(dict_to_save, f)

def load_dict(file_path):
    with open(file_path,'rb') as f:
        return pickle.load(f)

test_dict = {
    1 : 'a',
    2 : 'b',
    3 : 'c'
}

save_dict(test_dict,'test_dict.pickle')
print(load_dict('test_dict.pickle'))


# saving the CSV
save_dict(test_dict,'test_dict.csv')
print(load_dict('test_dict.csv'))

# saving the Json
save_dict(test_dict,'test_dict.json')
print(load_dict('test_dict.json'))

