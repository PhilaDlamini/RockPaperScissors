'''The player'''

class Player:
    
    @staticmethod
    def decide():
        print("Choose 'Rock', 'Paper', or 'Scissors'")
        choice = input().capitalize().strip();
        
        while choice != 'Rock' and choice != 'Paper' and choice != 'Scissors':
            print('Please enter a valid choice');
            choice = input().capitalize().strip();
            
        return choice;
        