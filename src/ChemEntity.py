## @file ChemEntity.py
#  @author Sam (Jia Wei) Liu
#  @brief Module that creates the ChemEntity ABC
#  @date 02/08/2020

from abc import ABC, abstractmethod


## @brief An abstract base class that is inherited
class ChemEntity(ABC):

    ## @brief Finds the number of atoms of a specific element
    #  @param elm an element of type ElementT
    @abstractmethod
    def num_atoms(self, elm):
        pass

    ## @brief Compiles a set of elements in a Molecule or CompoundT object
    @abstractmethod
    def constit_elems(self):
        pass
