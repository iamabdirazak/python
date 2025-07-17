class house:
    def __init__(self, windows, doors):
        self.windows: int = windows
        self.doors: int = doors

    def open_window(self):
        return print(f'My house has {self.windows} windows and {self.doors} doors')

new_house: house = house(2, 1)

new_house.open_window()
