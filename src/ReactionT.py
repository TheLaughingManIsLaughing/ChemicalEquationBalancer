## @file ReactionT.py
#  @author Sam (Jia Wei) Liu
#  @brief Calculates the coefficients in a chemical reaction forumla
#  @date 02/08/2020

import numpy as np


## @brief Abstract data type that represents a chemical formula
class ReactionT:

    ## @brief ReactionT constructor
    #  @details Initializes ReactionT whose state variables contain the
    #  left hand side and right hand side of the chemical formula, as well
    #  as the calculated coefficients for each side. Uses Python's numpy module
    #  calculate the coefficients
    #  @param L Represents the left hand side of the chemical reaction as a list
    #  of CompoundT objects
    #  @param R Represents the right hand side of the chemical reaction as a list
    #  of CompoundT objects
    #  @throws ValueError if the set of ElementT objects on both sides do not match.
    #  Also if the coefficient matrix formed cannot be calculated due to it being not
    #  square or non-invertible
    def __init__(self, L, R):
        mol_l_set = set()
        mol_r_set = set()
        for ct_l in L:
            for elem_t in (ct_l.constit_elems().to_seq()):
                mol_l_set.add(elem_t)

        for ct_r in R:
            for elem_t in (ct_r.constit_elems().to_seq()):
                mol_r_set.add(elem_t)

        if (set(mol_l_set) != set(mol_r_set)):
            raise ValueError

        a_array = list()
        for elem_t in mol_l_set:
            a_row = list()
            for ct_l in L:
                if (elem_t in set(ct_l.constit_elems().to_seq())):
                    a_row.append(ct_l.num_atoms(elem_t))
                else:
                    a_row.append(0)
            for ct_r in R:
                if (elem_t in set(ct_r.constit_elems().to_seq())):
                    a_row.append(-1 * (ct_r.num_atoms(elem_t)))
                else:
                    a_row.append(0)
            a_array.append(a_row)

        x_array = [0] * (len(L) + len(R) - 1)
        x_array.append(1)
        a_array.append(x_array)

        b_array = [[0]] * (len(a_array) - 1)
        b_array.append([1])

        a_matrix = np.array(a_array)
        b_matrix = np.array(b_array)
        try:
            x_matrix = np.linalg.solve(a_matrix, b_matrix)
        except:
            raise ValueError

        coeff_l = list()
        coeff_r = list()
        for coeff in range(len(x_matrix)):
            if coeff < len(L):
                coeff_l.append(x_matrix[coeff][0])
            else:
                coeff_r.append(x_matrix[coeff][0])

        self.lhs = L
        self.rhs = R
        self.coeff_l = coeff_l
        self.coeff_r = coeff_r

    ## @brief Getter function for the left hand side of the chemical reaction
    #  @return List of CompoundT objects
    def get_lhs(self):
        return self.lhs

    ## @brief Getter function for the right hand side of the chemical reaction
    #  @return List of CompoundT objects
    def get_rhs(self):
        return self.rhs

    ## @brief Getter function for the coefficients on the left hand side
    #  @return List of integer values 
    def get_lhs_coeff(self):
        return self.coeff_l

    ## @brief Getter function for the coefficients on the right hand side
    #  @return List of integer values
    def get_rhs_coeff(self):
        return self.coeff_r
