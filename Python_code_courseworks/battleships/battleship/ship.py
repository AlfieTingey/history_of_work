class Ship(object):
    """
    Representing the ships that are placed on the board
    """


    def __init__(self,
                 coord_start: tuple,
                 coord_end: tuple):
        """
        Creates a ship given its start and end coordinates on board (the order does not matter)
        :param coord_start: tuple of 2 positive integers representing the starting position of the Ship on the board
        :param coord_end: tuple of 2 positive integers representing the ending position of the Ship on the board
        :raise ValueError: if the ship is neither horizontal nor vertical
        """

        self.x_start, self.y_start = coord_start
        self.x_end, self.y_end = coord_end

        self.x_start, self.x_end = min(self.x_start, self.x_end), max(self.x_start, self.x_end)
        self.y_start, self.y_end = min(self.y_start, self.y_end), max(self.y_start, self.y_end)

        if not self.is_horizontal() and not self.is_vertical():
            raise ValueError("The ship_1 needs to have either a horizontal or a vertical orientation.")

        self.set_coordinates_damages = set()
        self.set_all_coordinates = self.get_all_coordinates()

    def __len__(self):
        return self.length()

    def __repr__(self):
        return f"Ship(start=({self.x_start},{self.y_start}), end=({self.x_end},{self.y_end}))"

    @classmethod
    def get_ship_from_str_coordinates(cls, coord_str_start: str, coord_str_end: str) -> 'Ship':
        from battleship.convert import get_tuple_coordinates_from_str
        return cls(coord_start=get_tuple_coordinates_from_str(coord_str_start),
                   coord_end=get_tuple_coordinates_from_str(coord_str_end))

    def is_vertical(self) -> bool:
        """
        :return: True if and only if the direction of the ship is vertical
        """
        # TODO
        return self.x_start == self.x_end

    def is_horizontal(self) -> bool:
        """
        :return: True if and only if the direction of the ship is horizontal
        """
        # TODO
        return self.y_start == self.y_end

    def length(self) -> int:
        """"
        :return: The number of positions the ship takes on Board
        """
        # TODO
        if self.y_start == self.y_end:
            return int(self.x_end - self.x_start + 1)
        elif self.x_start == self.x_end:
            return int(self.y_end - self.y_start + 1)

    def is_on_coordinate(self,
                         coord_x: int,
                         coord_y: int
                         ) -> bool:
        """
        :param coord_x: integer representing the projection of a coordinate on the x-axis
        :param coord_y: integer representing the projection of a coordinate on the y-axis
        :return: True if and only if the ship if (coord_x, coord_y) is one of the coordinates of the ship
        """
        # TODO
        if coord_x == self.x_start:
            return coord_y <= self.y_end and coord_y >= self.y_start
        elif coord_y == self.y_start:
            return coord_x <= self.x_end and coord_x >= self.x_start

    def gets_damage_at(self,
                       coord_damage_x: int,
                       coord_damage_y: int
                       ) -> None:
        """
        The ship gets damaged at the point (coord_damage_x, coord_damage_y)
        :param coord_damage_x: integer representing the projection of a coordinate on the x-axis
        :param coord_damage_y: integer representing the projection of a coordinate on the y-axis
        """
        # TODO

        if self.is_on_coordinate(coord_damage_x,coord_damage_y):
            self.set_coordinates_damages.add((coord_damage_x,coord_damage_y))

        return self.set_coordinates_damages


    def is_damaged_at(self,
                      coord_x: int,
                      coord_y: int,
                      ) -> bool:
        """
        :param coord_x: integer representing the projection of a coordinate on the x-axis
        :param coord_y: integer representing the projection of a coordinate on the y-axis
        :return True if and only if the ship is damaged at (coord_x, coord_y)
        """
        # TODO
        return (coord_x, coord_y) in self.set_coordinates_damages


    def number_damages(self) -> int:
        """
        :return: The total number of coordinates at which the ship is damaged
        """
        # TODO
        return int(len(self.set_coordinates_damages))

    def has_sunk(self) -> bool:
        """
        :return: True if and only if ship is damaged at all its positions
        """
        # TODO
        return self.number_damages() == self.length()


    def get_all_coordinates(self) -> set:
        """
        :return: A set containing only all the coordinates of the ship
        """
        # TODO
        self.ship_coordinates = []
        for i in range(self.length()):
            if self.is_vertical():
                self.ship_coordinates.append((self.x_start, self.y_start + i))
            elif self.is_horizontal():
                self.ship_coordinates.append((self.x_start + i, self.y_start))

        return set(self.ship_coordinates)



    def is_near_coordinate(self, coord_x: int, coord_y: int) -> bool:
        """
        Tells if the ship is near a coordinate or not.

        In the example below:
        - There is a ship of length 3 represented by the letter S.
        - The positions 1, 2, 3 and 4 are near the ship
        - The positions 5 and 6 are NOT near the ship

        --------------------------
        |   |   |   |   | 3 |   |
        -------------------------
        |   | S | S | S | 4 | 5 |
        -------------------------
        | 1 |   | 2 |   |   |   |
        -------------------------
        |   |   | 6 |   |   |   |
        -------------------------


        :param coord_x: integer representing the projection of a coordinate on the x-axis
        :param coord_y: integer representing the projection of a coordinate on the y-axis
        :return: True if and only if (coord_x, coord_y) is at a distance of 1 of the ship OR is at the
        corner of the ship
        """
        return self.x_start - 1 <= coord_x <= self.x_end + 1 \
               and self.y_start - 1 <= coord_y <= self.y_end + 1

    def is_near_ship(self, other_ship: 'Ship') -> bool:
        """
        :param other_ship: other object of class Ship
        :return: True if and only if there is a coordinate of other_ship that is near this ship.
        """
        ship_near = False
        if other_ship.x_start == other_ship.x_end:
            for i in range(int(other_ship.y_end - other_ship.y_start + 1)):
                if self.is_near_coordinate(other_ship.x_start, other_ship.y_start + i):
                    ship_near = True
        elif other_ship.y_start == other_ship.y_end:
            for i in range(int(other_ship.x_end - other_ship.x_start + 1)):
                if self.is_near_coordinate(other_ship.x_start + i, other_ship.y_start):
                    ship_near = True

        return ship_near

if __name__ == '__main__':
    # SANDBOX for you to play and test your functions

    ship = Ship(coord_start=(3, 3), coord_end=(3, 5))
    print(ship.is_vertical())
    print(ship.is_horizontal()) # added by me
    print(ship.is_near_coordinate(7, 3))
    print(ship.length()) # added by me
    print(ship.is_on_coordinate(4,3), ship.is_on_coordinate(10,3)) # added by me
    ship.gets_damage_at(4, 3)
    ship.gets_damage_at(10, 3)
    print(ship.is_damaged_at(4, 3), ship.is_damaged_at(5, 3), ship.is_damaged_at(10, 3))

    # all 3 below added by me:
    print(ship.number_damages())
    print(ship.has_sunk())
    print(ship.get_all_coordinates())

    ship_2 = Ship(coord_start=(3,6), coord_end=(3,7))
    print(ship.is_near_ship(ship_2))
