#Object Oriented program
'''
Object - Any real life entity represented in code
For example students, cark, fruits
Class - Blueprint of an object
Example Class Fruits
Example - Banana, Mango, Apple, Grapes, Blueberries, Strawberries
'''

class fruit:
    # Attributes/vProperties of Class
    def __init__(self, color, taste, shape, prefrence):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.prefrence = prefrence

        # 2 class methods

        # 1. Getters
        def get_shape(shape, self):
            return self.shape

        def set_shape(shape, newshape):
            self.shape = newshape

        def increase_prefrence(self):
            self.prefrence = self.prefrence + 1
            
        def show_fruit(self):
            print("Hello, I am a fruit that is not existant in the dimention you are: {}, {}, {}, {}").format(self.color, self.shape, self.taste, self.prefrence)

apple = fruit("red", "crunchy, and sweet", "heart or round", 1)
apple.show_fruit()