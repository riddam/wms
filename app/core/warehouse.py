import json
import pathlib
from collections import defaultdict
from .containers import containers_types


class Warehouse:

    def __init__(self):
        self.capacity = Warehouse.load_warehouse_capacity()
        self.inventory = []
        self.archive = []
        self.containertypes = containers_types

    def get_capacity(self):
        """
        get warehouse maximum capacity
        :return: dictionary of warehouse max limits
        """
        return self.capacity

    def add_container(self, idx: int):
        """
        add container to the warehouse
        :param idx: container index in container types
        :return:
        """
        container = self.containertypes[idx]()
        try:
            Warehouse.add_container_params(container)
            self.inventory.append(container)
            print(f'Container {container} added successfully')

        except Exception:
            print(f'Failed to add container {type(container).__name__}')

    def search_container(self, container_id: int):
        """
        search container in the warehouse inventory
        :param container_id: search container id
        :return: position of the container in inventory list
        """
        for idx, container in enumerate(self.inventory):
            if container.id == container_id:
                return idx
        else:
            return None

    def remove_container(self, index):
        """
        remove container from warehouse to deliver
        :param index: positon of container in inventory
        :return: container object
        """
        container = self.inventory.pop(index)
        self.archive.append(container)
        return container

    def display_inventory(self):
        """
        Display container of each type available in warehouse
        :return:
        """
        inventory_dict = defaultdict(int)
        print(self.inventory)
        for container in self.inventory:
            inventory_dict[type(container).__name__] += 1
        print("Containers count of each type: ")
        for key, value in inventory_dict.items():
            print(f"{key} : {value}")
        print(f"total containers: {len(self.inventory)}")

    @staticmethod
    def add_container_params(obj):
        """
        Populate container attribute with validation
        :param obj: continer instance
        :return:
        """
        for attribute, valueconv in obj.attr.items():
            val = input(f"Enter {attribute}: ")
            val = valueconv(val)
            if val:
                setattr(obj, attribute, val)
            else:
                print(f'invalid value for {attribute}')
                raise Exception

    @staticmethod
    def load_warehouse_capacity() -> dict:
        """
        load warehouse capacity from json file
        :return: configuration dict
        """
        json_path = pathlib.Path('warehouse_config.json')
        with open(json_path) as f:
            config_data = json.load(f)
            data = config_data
        return data
