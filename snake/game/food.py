import random
from game import constants
from game.actor import Actor
from game.point import Point


# place an apple on the board in a random location.
# Render it on the board

#snake’s head runs over the apple and eats it
   
    # player eats an apple
    # remove it 
    #  generate a new apple
        # new random location
# When the player eats an apple, extend their body by 1 square

# When the player eats an apple, increment their score by 1
    #Remove the apple,
    #  generate a new apple
        # new random location
#make the snake’s body 1 square longer.

# When the player dies, tell them how many points they scored



class Food: #  inherit the properties and methods from the Actor class
    """ the program must have a Food class in addition to what is already provided.
        The Food class must inherit from Actor.
        The Food class must have one attribute called _points (an integer).
        The Food class must have one public method called reset.

        The responsibility of Food is to keep track of its appearance and position. 
        Food can move around randomly if asked to do so.
"""
    def __init__(self,_points, text, position, velocity):
        super().__init__()
        self._points = _points
        self.positon = position
        self.velocity= velocity
        self.text = "@"
        self.food = random 
    
    def reset(self):
        pass


# TODO: Define the Food class here

    def _handle_food_collision(self):
        """ Handles collisions between the snake's head and the food. Grows the snake, 
            updates the score and moves the food if there is one.
            Args:
                self"""
        pass
    def get_points(self):
        pass
    def get_position(self):
        pass
    def get_reset(self):
        while True:
            new_apple_loc = (
                random.randint(0, self.width-1),
                random.randint(0, self.height-1),
            )
            if new_apple_loc not in self.snake.body:
                break

        self.current_apple = Apple(new_apple_loc)

        pass