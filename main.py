'''Rock paper scissors game :)'''
from Computer import Computer;
from Player import Player;
from Decider import Decider;

#Decides the winner
def main():
    player = Player.decide();
    computer = Computer.decide();
    print('The computer chose ', computer, '. You chose ', player, sep = '');
    decider = Decider(computerChoice = computer, playerChoice = player);
    decider.decide();
     
print('Welcome to Rock Paper Scissors!!');
playAgain = 'Y';

while playAgain == 'Y':
    main();
    playAgain = input('Play again? Y/N\n');