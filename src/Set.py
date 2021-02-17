## @file Set.py
#  @author Sam (Jia Wei) Liu
#  @brief Module that creates the Set ADT
#  @date 02/08/2020

from Equality import Equality


## @brief An abstract data type that represents a set
#  of generic type
class Set(Equality):

    ## @brief Set constructor
    #  @details Initializes a Set object whose state
    #  is a set
    #  @param s Represents a list of elements
    def __init__(self, s):
        self.s = set(s)

    ## @brief Modifies the state variable by adding 
    #  the input into it
    #  @param e Represents the input of generic type
    def add(self, e):
        self.s.add(e)

    ## @brief Modifies the state variable by removing
    #  a specific element if it exists
    #  @param e Represents the input of generic type
    #  @throws ValueError if the state variable does not contain
    #  the input
    def rm(self, e):
        if (e in self.s):
            self.s.remove(e)
        else:
            raise ValueError

    ## @brief Checks if the input is in the state variable
    #  @param e Represents the input of generic type
    #  @return Boolean representing if input is in state variable or not
    def member(self, e):
        if (e in self.s):
            return True
        else:
            return False

    ## @brief Checks how many elements are in the state variable
    #  @return Integer value of number of elements
    def size(self):
        return len(self.s)

    ## @brief Checks if another Set object has the same elements
    #  @param T Represents another Set object
    #  @return Boolean representing if input matches the state variable
    def equals(self, T):
        if self.s == set(T.to_seq()):
            return True
        else:
            return False

    ## @brief Turns the state variable into type list
    #  @return The state variable as a list
    def to_seq(self):
        return list(self.s)
