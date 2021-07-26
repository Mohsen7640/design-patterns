class Cinema:
    pass


class Movie:
    pass


class Time:
    pass


class Hall:

    def __init__(self, name, cinema, capacity):
        self.name = name
        self.cinema = cinema
        self.capacity = capacity


class Seat:

    def __init__(self, number):
        self.number = number
        self.status = None


class Sens:

    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall

        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):

        for seat_number in range(1, self.hall.capacity + 1):
            self.seats.append(Seat(number=seat_number))
