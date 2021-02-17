## @file Equality.py
#  @author Sam (Jia Wei) Liu
#  @brief Module that creates the Equality ABC
#  @date 02/08/2020

from abc import ABC, abstractmethod


## @brief An abstract base class that is inherited
class Equality(ABC):

    ## @brief Checks if state variable and input are equal
    #  @param T Represents a generic type
    @abstractmethod
    def equals(self, T):
        pass
