from ..validators import validate_int, validate_float


class Container:
    container_id = 0

    def __init__(self):
        self.length = None,
        self.width = None
        Container.container_id += 1

    def __del__(self):
        Container.container_id -= 1


class Box(Container):
    attr = {'length': validate_int,
            'width': validate_int,
            'depth': validate_int}

    def __init__(self):
        super().__init__()
        self.depth = None
        self.id = Container.container_id

    def deliver(self):
        """
        delivery and shipping of box using Car
        :return:
        """
        print(f'Box {self.id} delivered by Car')

    def __repr__(self):
        return f"Normal Box: {self.id}"

    def __str__(self):
        return f"Normal Box: {self.id}"


class ColdBox(Box):
    attr = {'length': validate_int,
            'width': validate_int,
            'depth': validate_int,
            'temp': validate_float}

    def __init__(self):
        super().__init__()
        self.temp = None
        self.id = Container.container_id

    def __repr__(self):
        return f"Cold Box: {self.id}"

    def __str__(self):
        return f"Cold Box: {self.id}"


class Bag(Container):
    attr = {'length': validate_int,
            'width': validate_int,
            'weight': validate_int}

    def __init__(self):
        super().__init__()
        self.weight = None
        self.id = Container.container_id

    def deliver(self):
        """
        delivery and shipping of bag using Bike
        :return:
        """
        print(f'Bag {self.id} delivered by Bike')

    def __str__(self):
        return f"Bag({self.id})"

    def __repr__(self):
        return f"Bag: {self.id}"
