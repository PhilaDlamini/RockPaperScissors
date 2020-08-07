''''The computer player'''
from random import randint;

class Computer:
    
    #Maps the randomly generated value to one of these
    __values = {1: 'Rock', 2: 'Paper', 3: 'Scissors'};
    
    @staticmethod
    def decide():
        number = randint(1, 3);
        return Computer.__values[number];
      
