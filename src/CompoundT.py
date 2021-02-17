## @file CompoundT.py
#  @author Sam (Jia Wei) Liu
#  @brief Module that creates a CompoundT object
#  @date 02/08/2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet
from MolecSet import MolecSet


## @brief An abstract data type that represents a compound
class CompoundT(ChemEntity, Equality):

    ## @brief CompoundT constructor
    #  @details Initializes a CompoundT object whose state consists
    #  of a MolecSet object
    #  @param m MolecSet object
    def __init__(self, m):
        self.c = m

    ## @brief Getter function that returns the state variable
    def get_molec_set(self):
        return self.c

    ## @brief Calculates the number of a specific element in the state
    #  @param e Represents an element of type ElementT
    #  @return The number of elements in CompoundT
    def num_atoms(self, e):
        counter_atoms = 0
        for i in (self.c.to_seq()):
            if i.get_elm() == e:
                counter_atoms += i.get_num()
        return counter_atoms

    ## @brief Compiles a set of all unique elements in the state variable
    #  @return The set of all elements as an ElmSet
    def constit_elems(self):
        elmset = set()
        for i in (self.c.to_seq()):
            elmset.add(i.get_elm())
        return ElmSet(list(elmset))

    ## @brief Checks if another CompoundT object matches with state variable
    #  @param d Represents Input of type CompoundT
    #  @return Boolean representing if input matches with state variable or not
    def equals(self, d):
        if self.c.equals(d.get_molec_set()):
            return True
        else:
            return False
