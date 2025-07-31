from csv import DictReader

def house_data_loader(file_path):
    with open(file_path, mode='r', encoding='utf-8') as fh:
        reader = DictReader(fh)
        for row in reader:
            yield row


def city_filter(city_name, target):
    '''
        Based on the city name, gives us particular record
    '''
    try:
        while True:
            row = (yield)
            if row["City"] == city_name:
                target.send(row)
    except GeneratorExit:
        target.close()

def transform_data(target):
    try:
        while True:
            row = (yield)
            row["Rent"] = int(row["Rent"])
            # Size sqft -> sqm
            row["Size"] = float(row["Size"]) * 0.092903
            target.send(row)
    except GeneratorExit:
        target.close()

def data_sink():
    try:
        while True:
            row = (yield)
            print("Processed Row:", row)
    except GeneratorExit:
        print("Done Streaming....")

sink = data_sink()
next(sink)

transform = transform_data(sink)
next(transform)

filter_corout = city_filter("Kolkata", transform)
next(filter_corout)

for row in house_data_loader("./data/house_rent.csv"):
    filter_corout.send(row)

filter_corout.close()

# generator = house_data_loader("./data/house_rent.csv")

# for _ in range(5):
#     print(next(generator))