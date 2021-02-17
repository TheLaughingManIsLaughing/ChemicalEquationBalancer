## @file test_All.py
#  @author Sam (Jia Wei) Liu
#  @brief Tests implementation of python files Set, MoleculeT, CompoundT, and ReactionT.
#  @date 02/08/2020

from pytest import *
from ChemTypes import ElementT
from Set import Set
from ElmSet import ElmSet
from MolecSet import MolecSet
from MoleculeT import MoleculeT
from CompoundT import CompoundT
from ReactionT import ReactionT


## @brief Test methods for Set.py, also contains tests for ElmSet
class TestSetADT:

    def setup_method(self, method):
        set1 = [0, 1, 2, 3, 4, 5]
        self.setS = Set(set1)
        elmset1 = ElmSet([ElementT.Na, ElementT.Cl])
        elmset2 = ElmSet([ElementT.C, ElementT.O])
        elmset3 = ElmSet([ElementT.Cl, ElementT.Na])
        elmset4 = ElmSet([])
        self.elmset1 = elmset1
        self.elmset2 = elmset2
        self.elmset3 = elmset3
        self.elmset4 = elmset4

    def teardown_method(self, method):
        self.setS = None
        self.elmset1 = None
        self.elmset2 = None
        self.elmset3 = None

    def test_set_add1(self):
        self.setS.add(42)
        assert (self.setS.to_seq() == [0, 1, 2, 3, 4, 5, 42])

    def test_set_add2(self):
        self.setS.add(3)
        assert (self.setS.to_seq() == [0, 1, 2, 3, 4, 5])

    def test_set_rm1(self):
        self.setS.rm(0)
        assert (self.setS.to_seq() == [1, 2, 3, 4, 5])

    def test_set_rm2(self):
        with raises(ValueError):
            self.setS.rm(100)

    def test_set_rm3(self):
        self.setS.rm(3)
        assert (self.setS.to_seq() == [0, 1, 2, 4, 5])

    def test_set_member1(self):
        assert not(self.elmset1.member(ElementT.H) == True)

    def test_set_member2(self):
        assert (self.elmset1.member(ElementT.Na) == True)

    def test_size1(self):
        assert (self.elmset1.size() == 2)

    def test_size2(self):
        assert (self.elmset4.size() == 0)

    def test_equals1(self):
        assert not(self.elmset1.equals(self.elmset2) == True)

    def test_equals2(self):
        assert (self.elmset1.equals(self.elmset3) == True)


class TestMoleculeTADT:

    def setup_method(self, method):
        m1 = MoleculeT(1, ElementT.C)
        m2 = MoleculeT(2, ElementT.O)
        self.m1 = m1
        self.m2 = m2

    def teardown_method(self, method):
        self.m1 = None
        self.m2 = None

    def test_get_num(self):
        assert (self.m1.get_num() == 1)

    def test_get_elm(self):
        assert (self.m1.get_elm() == ElementT.C)

    def test_num_atoms1(self):
        assert (self.m2.num_atoms(ElementT.O) == 2)

    def test_num_atoms2(self):
        assert (self.m2.num_atoms(ElementT.Ca) == 0)

    def test_constit_elems(self):
        assert (self.m2.constit_elems().to_seq() == [ElementT.O])

    def test_equals1(self):
        assert not(self.m2.equals(self.m1) == True)

    def test_equals2(self):
        assert (self.m2.equals(MoleculeT(2, ElementT.O)) == True)


class TestCompoundTADT:

    def setup_method(self, method):
        m1 = MoleculeT(6, ElementT.C)
        m2 = MoleculeT(12, ElementT.H)
        m3 = MoleculeT(6, ElementT.O)
        m4 = MoleculeT(6, ElementT.H)
        c1 = CompoundT(MolecSet([m1, m2, m3]))
        c2 = CompoundT(MolecSet([m1, m2, m4]))
        c3 = CompoundT(MolecSet([m3, m1, m2]))
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def teardown_method(self, method):
        self.c1 = None
        self.c2 = None
        self.c3 = None

    def test_get_molec_set(self):
        assert (((self.c1).get_molec_set()).equals((self.c3).get_molec_set()) == True)

    def test_num_atoms1(self):
        assert (self.c1.num_atoms(ElementT.H) == 12)

    def test_num_atoms2(self):
        assert (self.c2.num_atoms(ElementT.H) == 18)

    def test_constit_elems1(self):
        assert (self.c1.constit_elems().equals(ElmSet([ElementT.C, ElementT.H, ElementT.O])) == True)

    def test_constit_elems2(self):
        assert (self.c2.constit_elems().equals(ElmSet([ElementT.C, ElementT.H])) == True)

    def test_equals1(self):
        assert not(self.c1.equals(self.c2) == True)

    def test_equals2(self):
        assert ((self.c1).equals(self.c3) == True)


class TestReactionTADT:

    def setup_method(self, method):
        h2 = MoleculeT(2, ElementT.H)
        o1 = MoleculeT(1, ElementT.O)
        c_h2 = CompoundT(MolecSet([h2]))
        c_o1 = CompoundT(MolecSet([o1]))
        c_h2_o1 = CompoundT(MolecSet([h2, o1]))
        lhs1 = [c_h2, c_o1]
        rhs1 = [c_h2_o1]
        self.lhs1 = lhs1
        self.rhs1 = rhs1

        m1 = MoleculeT(6, ElementT.C)
        m2 = MoleculeT(12, ElementT.H)
        m3 = MoleculeT(6, ElementT.O)
        m4 = MoleculeT(2, ElementT.O)
        m5 = MoleculeT(1, ElementT.C)
        m6 = MoleculeT(2, ElementT.H)
        m7 = MoleculeT(1, ElementT.O)
        c1 = CompoundT(MolecSet([m1, m2, m3]))
        c2 = CompoundT(MolecSet([m4]))
        c3 = CompoundT(MolecSet([m5, m4]))
        c4 = CompoundT(MolecSet([m6, m7]))
        lhs2 = [c1, c2]
        rhs2 = [c3, c4]
        self.lhs2 = lhs2
        self.rhs2 = rhs2

        m8 = MoleculeT(2, ElementT.Fe)
        m9 = MoleculeT(3, ElementT.O)
        m10 = MoleculeT(1, ElementT.Fe)
        c5 = CompoundT(MolecSet([m8, m9]))
        c6 = CompoundT(MolecSet([m5]))
        c7 = CompoundT(MolecSet([m10]))
        c8 = CompoundT(MolecSet([m5, m4]))
        lhs3 = [c5, c6]
        rhs3 = [c7, c8]
        self.lhs3 = lhs3
        self.rhs3 = rhs3

    def teardown_method(self, method):
        self.lhs1 = None
        self.rhs1 = None
        self.lhs2 = None
        self.rhs2 = None

    def test_get_lhs1(self):
        assert (ReactionT(self.lhs1, self.rhs1).get_lhs() == self.lhs1)

    def test_get_rhs1(self):
        assert (ReactionT(self.lhs1, self.rhs1).get_rhs() == self.rhs1)

    def test_get_lhs1_coeff(self):
        assert (ReactionT(self.lhs1, self.rhs1).get_lhs_coeff() == [1, 1])

    def test_get_rhs1_coeff(self):
        assert (ReactionT(self.lhs1, self.rhs1).get_rhs_coeff() == [1])

    def test_get_lhs2_coeff(self):
        assert (ReactionT(self.lhs2, self.rhs2).get_lhs_coeff() == [0.16666666666666666, 1.0])

    def test_get_rhs2_coeff(self):
        assert (ReactionT(self.lhs2, self.rhs2).get_rhs_coeff() == [1.0, 1.0])

    def test_get_lhs3_coeff(self):
        with raises(ValueError):
            ReactionT(self.lhs1, self.rhs2).get_lhs_coeff()

    def test_get_lhs4_coeff(self):
        assert (ReactionT(self.lhs3, self.rhs3).get_lhs_coeff() == [2, 3])

    def test_get_rhs4_coeff(self):
        assert (ReactionT(self.lhs3, self.rhs3).get_rhs_coeff() == [4, 3])
