#Mr Stark is facing the north. Peter is in trouble, and he is facing the south. Stark being his mentor will protect him as soon as he sees that Peter is in trouble.
#Stark's suit is programmed to rotate automatically in the direction of most enemies. By analyzing the direction in which most enemies are heading, the suit provides you with the next set of suit instructions in
#the form of a string S.
#When Stark faces south, he ignores the rest of his suit instructions and immediately goes to rescue Peter.
#Write a program that reads the set of suit instructions S and determines whether Stark will be able to save Peter.
#Note
#The string S contains either L or R. The letter L indicates left and the letter R indicates right.

#Code:
def can_save_peter(instructions: str) -> bool:
    direction = 'N'
    
    for instruction in instructions:
        if direction == 'N':
            if instruction == 'L':
                direction = 'W'
            elif instruction == 'R':
                direction = 'E'
        elif direction == 'E':
            if instruction == 'L':
                direction = 'N'
            elif instruction == 'R':
                direction = 'S'
        elif direction == 'S':
            return True
        elif direction == 'W':
            if instruction == 'L':
                direction = 'S'
            elif instruction == 'R':
                direction = 'N'
    return False
instructions = "LRLRRLL"
if can_save_peter(instructions):
    print("Stark will be able to save Peter.")
else:
    print("Stark will not be able to save Peter.")
