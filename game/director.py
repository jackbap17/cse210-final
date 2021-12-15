from time import sleep
import random
from game import constants
from game.create_cast import CreateCast

class Director:
    
    def __init__(self, cast, script):
        self._cast = cast
        self._script = script
        self.create_cast = CreateCast()
        self._i = 0
    


    def start_game(self):
        while True:
            self._cue_action("input")
            self._cue_action("update")
            if self._i == 2:
                self._i = 0 
                self.create_cast.create_missiles(self._cast)  
            self._i += 1       
            if random.randint(1,54) == 2:
                self.create_cast.create_aliens(self._cast)
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        for action in self._script[tag]:
            action.execute(self._cast)