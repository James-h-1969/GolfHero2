from constants import *

class Levels():
    def __init__(self):
        self.unlocked = [True, False, False, False, False, False, False, False, False]

    def unlock_hole(self) -> int:
        """
        holds record of how many holes have been played so far

        Args:
        self -> changes own property

        Returns:
        i: how many holes have been unlocked
        """
        for i in range(HOLES):
            if not self.unlocked[i]:
                self.unlocked[i] == True
                return i
        return HOLES
    
    def is_hole_unlocked(self, i: int) -> bool:
        """
        checks whether a specific hole is unlocked

        Args:
        i: what hole to check

        Returns:
        is_unlocked: boolean of whether locked or not
        """
        return self.unlocked[i-1]

    def play_level(self, i: int) -> None:
        """
        plays the level till exit or finish
        
        """
        print("Starting Level " + str(i) + " ! ")


