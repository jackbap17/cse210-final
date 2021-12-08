import random
import sys
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class HandleCollisionsAction(Action):

    def execute(self, cast):
        ship = cast["ship"][0]
        missiles = cast["missiles"] 
        aliens = cast["aliens"]

        for alien in aliens:
            for missile in missiles:
                if missile.get_position().equals(alien.get_position()):
                    alien.set_text(" ")
                    missile.set_text(" ")

