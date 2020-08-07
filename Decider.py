''''Decides the winner'''
class Decider:
    
    #All possible combinations
    combination1 = ['Rock', 'Paper'];
    combination2 = ['Paper', 'Scissors'];
    combination3 = ['Scissors', 'Rock'];
    
    def __init__(self, computerChoice, playerChoice):
        self.computerChoice = computerChoice;
        self.playerChoice = playerChoice;
    
    def decide(self):
        if self.computerChoice == self.playerChoice:
            print("It's a draw!!");
        else:
            if self.computerChoice in self.combination1 and self.playerChoice in self.combination1:
                self.announceWinner(self.combination1);
            elif self.computerChoice in self.combination2 and self.playerChoice in self.combination2:
                self.announceWinner(self.combination2);
            else:
                self.announceWinner(self.combination3);
                
    def announceWinner(self, combination):
        if self.playerChoice == combination[1]: 
            print('You are the winner!!');
        else:
            print('The computer wins!!');
        
            
            