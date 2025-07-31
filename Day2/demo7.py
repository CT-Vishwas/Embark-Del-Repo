from csv import DictReader

def house_data_loader(file_path):
    with open(file_path, mode='r', encoding='utf-8') as fh:
        reader = DictReader(fh)
        for row in reader:
            yield row

generator = house_data_loader("./data/house_rent.csv")

for _ in range(5):
    print(next(generator))