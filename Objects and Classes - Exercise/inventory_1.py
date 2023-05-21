class Inventory:
    __capacity = 0

    def __init__(self, __capacity):
        self.__capacity = int(__capacity)
        self.items = []

    def add_item(self, item):
        if (self.__capacity - len(self.items)) > 0:
            self.items.append(str(item))
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(ch for ch in self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)