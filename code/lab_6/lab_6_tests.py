import pytest
from furniture import Furniture
from room import Room

@pytest.fixture
def room():
    return Room([10, 10])

@pytest.fixture
def wardrobe():
    return Furniture("Шафа-купе", [3, 5], [1, 4]) 

@pytest.fixture
def sofa():
    return Furniture("Диван", [6, 7], [5, 2])

def test_furniture_creation(wardrobe):
    assert wardrobe.name == 'Шафа-купе'
    assert wardrobe.coordinates == [3, 5]
    assert wardrobe.size == [1, 4]

def test_room_creation(room):
    assert room.size_room == [10, 10]
    assert room.object == []

def test_add_object_to_room(room,wardrobe):
    room.add_object(wardrobe)
    assert room.object == [wardrobe]
    assert wardrobe.name == "Шафа-купе"

def test_check_size_within_room(room, wardrobe):
    assert room.check_size(wardrobe) is True

def test_check_size_outside_room(room, sofa):
    assert room.check_size(sofa) is False

def test_remove_object(room, wardrobe):
    room.add_object(wardrobe)
    room.remove_object(wardrobe)
    assert room.object == []

def test_remove_nonexistent_object(room, wardrobe):
    room.remove_object(wardrobe)
    assert room.object == []

def test_rearrangment_if_furniture_added(room,wardrobe):
    room.add_object(wardrobe)
    room.rearrangement('Шафа-купе', [6, 6])
    assert room.object == [wardrobe]
    assert wardrobe.coordinates == [6, 6]

def test_rearrangment_if_furniture_not_added(room,wardrobe):
    room.rearrangement('Шафа-купе', [6, 6])
    assert room.object == []

def test_rearrangment_if_room_empty(room):
    room.rearrangement('Шафа-купе', [6, 6])
    assert room.object == []

def test_find_object_exists(room, wardrobe):
    room.add_object(wardrobe)
    assert room.find_object('Шафа-купе') == wardrobe

def test_find_object_not_exists(room):
    assert room.find_object('Шафа-купе') is None

def test_display_info_empty_room(capsys, room):
    room.display_info()
    captured = capsys.readouterr()
    assert captured.out == ''

# def test_display_info_with_objects(capsys, room, wardrobe, sofa):
#     room.add_object(wardrobe)
#     room.add_object(sofa)
#     room.display_info()
#     captured = capsys.readouterr()
#     expected_output = " Об*єкт Шафа-купе має координати [3, 5] та розмір [1, 4] \n Об*єкт Диван має координати [6, 7] та розмір [5, 2] \n"
#     assert captured.out == expected_output
