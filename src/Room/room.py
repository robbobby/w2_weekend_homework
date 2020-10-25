from src.Room.room_types import RoomType


class Room:
    def __init__(self, rooms, dukebox, room_quality):
        self.dukebox = dukebox
        self.rooms = rooms
        self.quality = room_quality
        self.atmosphere = 0
        self.guests = []
        self.guest_limit = 0
        self.__set_rooms_quality()

        self.set_atmosphere()

    def add_room(self, room):
        self.rooms.append(room)
        self.set_atmosphere()

    def set_atmosphere(self):
        if len(self.rooms) > 0:
            self.atmosphere = 0
            for room in self.rooms:
                self.atmosphere += room.atmosphere
            self.atmosphere / len(self.rooms)

    def add_guest(self, customer):
        for guest in self.guests:
            if guest == customer:
                self.guests.remove(guest)
        self.guests.append(customer)

    def remove_guest(self):
        if len(self.guests) > 0:
            for guest in self.guests:
                self.guests.remove(guest)

    def is_big_enough(self, customer):
        if customer.partner != None and self.quality != RoomType.SINGLE:
            return True
        else:
            return False

    def __set_rooms_quality(self):
        if len(self.rooms) > 0:
            for room in self.rooms:
                room.quality = self.quality
                room.set_atmosphere()
        self.set_atmosphere()