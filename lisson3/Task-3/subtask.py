class address:
    def __init__(self, index, city, street, house, appartament):
        self.index=index
        self.city=city
        self.street=street
        self.house=house
        self.appartament=appartament

class mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track