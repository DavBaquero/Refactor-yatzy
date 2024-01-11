class Yatzy:

    @staticmethod
    def chance(*numbers):
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        
        Fixes:
        - Make a loop which can accept multiple values
        - Delete arguments (d1, d2, ...)
        '''
        
        total = 0
        for number in numbers:
            total += number
        return total

    @staticmethod
    def yatzy(dices):
        
        '''
        Code smells:
        - A loop is too long and too deeply nested
        
        Fixes:
        - Simplify the function
        - Make the code readable and undestandable
        '''
        
        firstDice = dices[0]
        for dice in dices:
            if dice == firstDice:
                continue
            else:
                return 0
        return  50

    @staticmethod
    def ones(*numbers):

        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 3:
                sum += 3
        return sum
    
    def fours(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 4:
                sum += 4
        return sum

    def fives(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 5:
                sum += 5
        return sum
    

    def sixes(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 6:
                sum += 6
        return sum
    
    @staticmethod
    def score_pair(*dices):
        
        '''
        adsadas
        '''
        
        dices_sorted = list(sorted(dices, reverse=True))
        for number in dices_sorted:
            if dices.count(number) >= 2:
                return number*2
        return 0

    
    @staticmethod
    def two_pair(*dices):

        '''
        sbnfahfioadf
        '''

        pair_counter = []
        for number in dices:
            if dices.count(number) >= 2 and number not in pair_counter:
                pair_counter.append(number)
                if len(pair_counter) == 2:
                    return sum(pair_counter) * 2
        return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dices):
        
        '''
        añjhsfijasfiojad
        '''
        
        dices_sorted = list(sorted(dices, reverse=True))
        for number in dices_sorted:
            if dices.count(number) >= 3:
                return number*3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0