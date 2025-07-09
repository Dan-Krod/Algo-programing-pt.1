import logging

class FurnitureError(Exception):
    pass


class SizeExceededException(FurnitureError):
    pass


class ObjectNotExistException(FurnitureError):
    def __init__(self, furniture_name):
        self.furniture_name = furniture_name
        super().__init__(f"Об*єкт {self.furniture_name} не знайдено в кімнаті")

# class RearrangementException(FurnitureError):
#     pass


def logged(exception, mode):
    logger = logging.getLogger(__name__)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as error:
                
                if mode == 'console':
                    logging.error(f"Exception '{exception.__name__}': {str(error)}")
                elif mode == 'file':
                    with open("error_log.txt", "a") as file:
                        print(file)
                        file.write(f"Виникла помилка '{exception.__name__}': {error}\n")

                else:
                    raise ValueError("Invalid logging mode")
                raise

        return wrapper
    
    return decorator


class Furniture:
    def __init__(self, name = "", coordinates =[], size = []):
        self.name = name
        self.coordinates = coordinates
        self.size = size

    def __str__(self):
        return f" Об*єкт {self.name} має координати {self.coordinates} та розмір {self.size} "
    

class Room:
    def __init__(self, size_room = []):
        self.size_room = size_room
        self.object = []
    
    @logged(exception=SizeExceededException, mode='file')
    def add_object(self, furniture):
        if self.check_size(furniture):
            self.object.append(furniture)
            print(f"Об*єкт {furniture.name} додано до кімнати ")
        else:
            raise SizeExceededException(f"Об*єкт {furniture.name} НЕ додано до кімнати, бо не вміщається в кімнату")

        
    def check_size(self, furniture):
        x, y = furniture.coordinates
        width, height = furniture.size

        return 0 <= x < self.size_room[0] and 0 <= y < self.size_room[1] and x + width <= self.size_room [0] and y + height <= self.size_room [1]

    @logged(exception=ObjectNotExistException, mode='console')               
    def remove_object(self, object_name):
        furniture = self.find_object(object_name)
        if furniture:
            self.object.remove(furniture)
            print(f"Об'єкт {object_name} видалено з кімнати")
        else:
            raise ObjectNotExistException(object_name)

    # @logged(exception=RearrangementException, mode='file')
    def rearrangement(self, object_name, new_coordinates):
        check_furniture = self.find_object(object_name)
        if check_furniture:
            if self.check_size(check_furniture):
                check_furniture.coordinates = new_coordinates
            else:
                # raise RearrangementException
                print(f"Об*єкт {check_furniture.name} не вміщається в кімнаті в кімнаті")
        else:
            raise ObjectNotExistException(f"Об*єкт {object_name} не знайдено в кімнаті")

    def find_object(self, name):
        for obj in self.object:
            if obj.name == name:
                return obj
        return None
    
    def display_info(self):
        for obj in self.object:
            print(obj)


def main():
    room_size = [10, 10]

    sofa = Furniture("Диван", [2, 3], [1, 4])
    wardrobe = Furniture("Шафа-купе", [1, 5], [2, 3])
    stelag = Furniture("Стелаж для книжок", [0, 8], [4, 7])

    room = Room(room_size)

    try:
        room.add_object(sofa)
        room.add_object(wardrobe)
        room.add_object(stelag)
    except FurnitureError as e:
        print(f"Caught exception: {e}")

    print('\nКімната на початку:')
    room.display_info()

    # try:
    room.rearrangement('Шафа-купе', [11, 3])
    # except RearrangementException as e:
    #     print(f"Caught exception: {e}")

    print('\nКімната після перестановки')
    room.display_info()

    try:
        room.remove_object(stelag.name)
    except ObjectNotExistException as e:
        print(f"Caught exception: {e}")


if __name__ == '__main__' :
    main()