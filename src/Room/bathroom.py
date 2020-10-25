from src.Room.room_types import RoomType


class Bathroom:
    def __init__(self, sink, bath, toilet, room_type):
        self.sink = sink
        self.bath = bath
        self.toilet = toilet
        self.room_type = room_type

        self.atmosphere = self.set_room_atmosphere()

    def set_room_atmosphere(self):
        return (self.toilet.atmosphere_level + self.bath.atmosphere_level +
                self.sink.atmosphere_level + self.room_quality()) // 4

    def room_quality(self):
        if self.room_type == RoomType.SINGLE:
            return 20
        if self.room_type == RoomType.DOUBLE:
            return 30
        if self.room_type == RoomType.TRIPLE:
            return 40
        if self.room_type == RoomType.DELUXE:
            return 60
        return 0