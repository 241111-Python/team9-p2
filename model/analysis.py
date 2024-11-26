class Analysis:
    def __init__(self, **kwargs):
        self.data = {}
    
    def add_entry(self, key: str, keys:list, values: list):
        self.data[key] = {}

        for k in range(len(keys)):
            self.data[key][keys[k]] = values[k]

        print("Entry added.")
    
    def __str__(self):
        for key in self.data.keys():
            for inKey, value in self.data[key].items():
                 print(f"{key}: {inKey} -> {value}")