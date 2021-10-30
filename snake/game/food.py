import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):
    """A nutritious substance that snake's like. The responsibility of Food is to keep track of its appearance and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.reset()
    
    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.
        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def reset(self):
        """Resets the food by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Food): an instance of Food.
        """
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)


# import random
# from game import constants
# from game.actor import Actor
# from game.point import Point


# # place an apple on the board in a random location.
# # Render it on the board

# #snake’s head runs over the apple and eats it
   
#     # player eats an apple
#     # remove it 
#     #  generate a new apple
#         # new random location
# # When the player eats an apple, extend their body by 1 square

# # When the player eats an apple, increment their score by 1
#     #Remove the apple,
#     #  generate a new apple
#         # new random location
# #make the snake’s body 1 square longer.

# # When the player dies, tell them how many points they scored



# class Food: #  inherit the properties and methods from the Actor class
#     """ the program must have a Food class in addition to what is already provided.
#         The Food class must inherit from Actor.
#         The Food class must have one attribute called _points (an integer).
#         The Food class must have one public method called reset.

#         The responsibility of Food is to keep track of its appearance and position. 
#         Food can move around randomly if asked to do so.
# """
#     def __init__(self,_points, text, position, velocity):
#         super().__init__()
#         self._points = _points
#         self.positon = position
#         self.velocity= velocity
#         self.text = "@"
#         self.food = random 
    
#     def reset(self):
#         pass


# : Define the Food class here

#     def _handle_food_collision(self):
#         """ Handles collisions between the snake's head and the food. Grows the snake, 
#             updates the score and moves the food if there is one.
#             Args:
#                 self"""
#         pass

#     def get_reset(self):
#         while True:
#             new_apple_loc = (
#                 random.randint(0, self.width-1),
#                 random.randint(0, self.height-1),
#             )
#             if new_apple_loc not in self.snake.body:
#                 break

#         self.current_apple = Apple(new_apple_loc)

#         pass