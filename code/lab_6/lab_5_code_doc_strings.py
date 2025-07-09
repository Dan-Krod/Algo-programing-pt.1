"""
Module containing classes and functions for managing furniture in a room.

Classes:
- Furniture: Represents a piece of furniture with a name, coordinates, and size.
- Room: Represents a room with a specified size and the ability to add, 
rearrange, and remove furniture.

Functions:
- main: Demonstrates the functionality of the Room and Furniture classes.

Usage:
1. Create furniture objects with specific attributes.
2. Create a room object with a specified size.
3. Add furniture to the room using the add_object method.
4. Display information about the room and its furniture with the display_info method.
5. Rearrange furniture within the room using the rearrangement method.
6. Remove furniture from the room using the remove_object method.
"""

class Furniture:
    """
    The Furniture class represents furniture in a room.

    Parameters:
    - name (str): The name of the furniture.
    - coordinates (list): The coordinates of the furniture in the room.
    - size (list): The size of the furniture.

    Methods:
    - __init__: Initializes a Furniture object with the specified parameters.
    - __str__: Returns a string representation of the Furniture object.
    - display_info: Displays information about the furniture.
    """

    def __init__(self, name = "", coordinates =None, size = None):
        """
        Initializes a Furniture object.

        :param name: The name of the furniture.
        :param coordinates: The coordinates of the furniture in the form [x, y].
        :param size: The size of the furniture in the form [weight, hight].
        """

        self.name = name
        self.coordinates = coordinates
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the Furniture object.

        :return: A string representation of the furniture.
        """
        return f" Об*єкт {self.name} має координати {self.coordinates} та розмір {self.size} "

    def display_info(self):
        """
        Displays information about the furniture.

        :return: None
        """
        print(f"Інформація про мебель {self.name}:")
        print(f"Координати: {self.coordinates}")
        print(f"Розмір: {self.size}")

class Room:
    """
    The Room class represents a room containing furniture.

    Parameters:
    - size_room (list): The size of the room.
    
    Methods:
    - __init__: Initializes a Room object with the specified parameters.
    - add_object: Adds furniture to the room.
    - check_size: Checks if the Furniture object has correct size and coordinates in the room.
    - remove_object: Removes the Furniture object from the room.
    - rearrangement: Rearranges the Furniture object in the room to new coordinates.
    - find_object: Finds a Furniture object by name.
    - display_info: Displays information about all furniture in the room.
    """

    def __init__(self, size_room = None):
        """
        Initializes a Room object.

        :param size_room: The size of the room.
        """
        self.size_room = size_room
        self.object = []

    def add_object(self, furniture):
        """
        Adds a furniture object to the room if it fits.

        :param furniture: The furniture object to be added.
        """
        if self.check_size(furniture):
            self.object.append(furniture)
            print(f"Об*єкт {furniture.name} додано до кімнати " )
        else:
            print(f"Об*єкт {furniture.name} НЕ додано до кімнати, бо не вміщається в кімнату " )

    def check_size(self, furniture):
        """
        Checks if the furniture object fits within the room.

        :param furniture: The furniture object to be checked.
        :return: True if it fits, False otherwise.
        """
        x, y = furniture.coordinates
        width, height = furniture.size

        x_condition = 0 <= x < self.size_room[0]
        y_condition = 0 <= y < self.size_room[1]
        width_condition = x + width <= self.size_room[0]
        height_condition = y + height <= self.size_room[1]

        return x_condition and y_condition and width_condition and height_condition

    def remove_object(self, furniture):
        """
        Removes a furniture object from the room.

        :param furniture: The furniture object to be removed.
        """
        if furniture in self.object:
            self.object.remove(furniture)
            print(f"\nОб*єкт {furniture.name} видалено з кімнати")
        else:
            print(f"\nОб*єкт {furniture.name} не знайдено в кімнаті")

    def rearrangement(self, object_name, new_coordinates):
        """
        Rearranges the position of a furniture object in the room.

        :param object_name: The name of the furniture object to be rearranged.
        :param new_coordinates: The new coordinates for the furniture object.
        """
        check_furniture = self.find_object(object_name)
        if check_furniture:
            if self.check_size(check_furniture):
                check_furniture.coordinates = new_coordinates
            else:
                print(f"Об*єкт {check_furniture.name} не вміщається в кімнаті в кімнаті")
        else:
            print(f"Об*єкт {object_name} не знайдено в кімнаті")

    def find_object(self, name):
        """
        Finds a furniture object in the room by its name.

        :param name: The name of the furniture object to find.
        :return: The furniture object if found, None otherwise.
        """
        for obj in self.object:
            if obj.name == name:
                return obj
        return None

    def display_info(self):
        """
        Displays information about the furniture objects in the room.
        """
        for obj in self.object:
            print(obj)

def main():
    """
    Demonstrates the functionality of the Room and Furniture classes.

    Creates furniture objects (sofa, wardrobe, stelag) and a room object. 
    Adds furniture to the room,
    displays the room information, rearranges furniture, 
    displays the room information again,
    and finally removes a piece of furniture from the room.
    """
    room_size = [10, 10]

    sofa = Furniture("Диван", [2, 3], [1, 4])
    wardrobe = Furniture("Шафа-купе", [1, 5], [2, 3])
    stelag = Furniture("Стелаж для книжок", [0, 8], [4, 7])

    room = Room(room_size)

    room.add_object(sofa)
    room.add_object(wardrobe)
    room.add_object(stelag)

    print('\nКімната на початку:')
    room.display_info()

    room.rearrangement('Шафа-купе', [6,5])

    print('\nКімната після перестановки')
    room.display_info()

    room.remove_object(sofa)


if __name__ == '__main__' :
    main()
