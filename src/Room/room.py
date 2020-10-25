class Room:
    def __init__(self, rooms, dukebox, room_quality):
        self.dukebox = dukebox
        self.rooms = rooms
        self.room_quality = room_quality
        self.atmosphere = 0
        self.set_atmosphere()
        self.guests = []
        self.guest_limit = 0

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
