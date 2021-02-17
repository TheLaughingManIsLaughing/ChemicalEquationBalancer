## @file MoleculeT.py
#  @author Sam (Jia Wei) Liu
#  @brief Module that creates the MoleculeT ADT
#  @date 02/08/2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet


## @brief An abstract data type that represents a molecule
class MoleculeT(ChemEntity, Equality):

    ## @brief MoleculeT constructor
    #  @details Initializes a MoleculeT object whose state
    #  has an integer and an ElementT object
    #  @param num Integer value
    #  @param elm ElementT object
    def __init__(self, num, elm):
        self.num = num
        self.elm = elm

    ## @brief Getter function that returns the number of ElementT
    #  as an integer
    def get_num(self):
        return self.num

    ## @brief Getter function that returns the ElementT object
    def get_elm(self):
        return self.elm

    ## @brief Checks if a certain ElementT object exists and returns
    #  its integer value
    #  @param elm Represents a ElementT object
    #  @return The integer value of the ElementT if input matches,
    #  otherwise integer 0 is returned
    def num_atoms(self, elm):
        if elm == self.elm:
            return self.num
        else:
            return 0

    ## @brief Compiles the ElementT state variable into an ElmSet
    #  @return ElmSet object
    def constit_elems(self):
        return ElmSet([self.elm])

    ## @brief Checks if the input is equal to the state variables
    #  @param m Represents another MoleculeT object
    #  @return A boolean representing if the state variables match or not
    def equals(self, m):
        if (self.elm == m.get_elm()) and (self.num == m.get_num()):
            return True
        else:
            return False
