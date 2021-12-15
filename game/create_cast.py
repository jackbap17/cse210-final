import random
from game import constants
from game.actor import Actor
from game.point import Point

class CreateCast():
    
   # def __init__(self, cast):
   #     self._cast = cast 

    def create_ship(self, cast):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        position = Point(x, y)
        ship = Actor()
        ship.set_text("A")
        ship.set_position(position)

        cast["ship"] = [ship]

    def create_missiles(self, cast):
        #cast["missiles"] = []
        ship = cast["ship"][0]
        position = ship.get_position()
        velocity = Point(0,-1)
        missile = Actor()
        missile.set_text("|")
        missile.set_position(position)
        missile.set_velocity(velocity)
        cast["missiles"].append(missile)

    def create_aliens(self, cast):
        #cast["aliens"] = []
        for x in range(random.randint(1,5)):
            position = Point(random.randint(1,35) *2, 2)
            velocity = Point(random.randint(-2,2),1)
            alien = Actor()
            alien.set_text("V")
            alien.set_position(position)
            alien.set_velocity(velocity)
            cast["aliens"].append(alien)




