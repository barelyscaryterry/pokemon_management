import json
import h5py
import csv
class PokeData:
    def __init__(self):
        #self.write_dict_to_hdf5()
        pass
    def fetch_data(self, key):
        with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", "r") as hdf5_file:
            json_string = hdf5_file["Pokemon"][key][()]
            return json.loads(json_string)
    def fetch_keys(self):
        keys = []
        with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", 'r') as f:
            group = f["Pokemon"]
            for key in group.keys():
                keys.append(key)
        return keys
    # def csv_to_dict(self):
    #     data = {}
    #     with open("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon_csv.csv") as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         for row in reader:
    #             name = row.pop("Name")
    #             row.pop("Legendary")
    #             data[name.lower()] = row
    #     return data
    
    # def write_dict_to_hdf5(self):
    #     data = self.csv_to_dict()
    #     with h5py.File("C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\dataset\\pokemon.hdf5", "w") as hdf5_file:
    #         hdf5_file.create_group("Pokemon")
    #         for name, values in data.items():
    #             values = json.dumps(values)
    #             hdf5_file["Pokemon"].create_dataset(name, data=values)

                
