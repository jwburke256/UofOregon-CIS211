"""These unit tests correspond directly to the examples in the HOWTO"""

import unittest
from university import *

# We'll use the same sample organization for all the provided tests,
# but do NOT assume that this is the only possible organization.

u_oregon = Composite("University of Oregon",
                     [Composite("College of Arts and Sciences",
                                [Composite("Division of Natural Sciences",
                                           [Unit("Department of Physics"),
                                            Unit("Department of Chemistry"),
                                            Unit("Department of Computer Science")]),
                                 Composite("Division of Social Sciences",
                                           [Unit("Department of Anthropology"),
                                            Unit("Department of Sociology"),
                                            Unit("Department of History")]),
                                 Composite("Division of Humanities",
                                           [Unit("Department of English"),
                                            Unit("Department of East Asian Languages")])]),
                      Composite("School of Music",
                                [Unit("Dance Department"),
                                 Unit("Music Performance")])])


class TestStep1(unittest.TestCase):
    """Part 1: return non-empty lists if we find the matching organization,
    corresponding to the first problem-solving step in the HOWTO)
    """
    def test_we_have_chemistry(self):
        """'Department of Chemistry' exists at UO"""
        chem = u_oregon.where_is("Department of Chemistry")
        self.assertTrue(len(chem) > 0, "Chemistry Department is found")

    def test_no_astrology(self):
        astrology = u_oregon.where_is("Department of Astrology")
        self.assertTrue(astrology == [], "There is no department of astrology, for some reason")


class TestStep2(unittest.TestCase):
    """Part 2:  Should also work for composite units like Division of Natural Sciences or School of Music"""
    def test_we_have_dance(self):
        """School of Music is a composite unit in the university"""
        music = u_oregon.where_is("School of Music")
        self.assertTrue(len(music) > 0, "We do have a school of music")

    def test_social_science(self):
        ss = u_oregon.where_is("Division of Social Sciences")
        self.assertTrue(len(ss) > 0, "We do have a division of social sciences in CAS")


class TestStep3(unittest.TestCase):
    """Tests for a complete solution, including composition of paths from a
    sub-organization up to the root of the organization.
    """
    def test_chem_path(self):
        """Chemistry is in the Division of Natural Sciences"""
        chem = u_oregon.where_is("Department of Chemistry")
        self.assertEqual(chem, ["Department of Chemistry",
                                "Division of Natural Sciences",
                                "College of Arts and Sciences",
                                "University of Oregon"])

    def test_humanities_path(self):
        humanities = u_oregon.where_is("Division of Humanities")
        self.assertEqual(humanities,
                         ["Division of Humanities",
                             "College of Arts and Sciences",
                             "University of Oregon"])


if __name__ == "__main__":
    unittest.main()
