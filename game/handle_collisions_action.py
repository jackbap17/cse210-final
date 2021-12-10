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
                    missile.set_text(' ')
                if missile.get_position().get_y() == 1:
                    missile.set_text(' ')

        a= 0                    
        for alien in aliens:
            if alien.get_text() == " ":
                cast["aliens"].pop(a)
            a +=1
        m = 0
        for missile in missiles:
            if missile.get_text == " ":
                cast["missiles"].pop(m)
            m +=1           

