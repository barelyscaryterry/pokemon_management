import json
import h5py
class InitDatabase:
    def __init__(self):
        pass
    def fetch_data(self, key):
        with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", 'r') as f:
            group = f['Pokemon']
            for k in group.keys():
                if k == key:
                    value = group[k][()]
                    try:
                        value = json.loads(value)
                    except:
                        pass
                    return value
    def fetch_keys(self):
        keys = []
        with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", 'r') as f:
            group = f['Pokemon']
            for key in group.keys():
                keys.append(key)
        return keys

                
