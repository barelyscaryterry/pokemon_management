import json
import h5py
import csv
class PokeData:
    def __init__(self):
        pass
        #self.write_dict_to_hdf5()
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
    def csv_to_dict(self):
        data = {}
        with open("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon_csv.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row.pop("Name")
                row.pop("Legendary")
                data[name] = row
        return data
    
    def write_dict_to_hdf5(self):
        data = self.csv_to_dict()
        with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", "w") as hdf5_file:
            for name, values in data.items():
                hdf5_file.create_group(name)
                for key, value in values.items():
                    hdf5_file[name].create_dataset(key, data=value)

                
