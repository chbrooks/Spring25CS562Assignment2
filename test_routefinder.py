from unittest import TestCase
from routefinder import *

class Testmap_state(TestCase):
    def test_is_lt (self) :
        s1 = map_state(g = 1,h=1)
        s2 = map_state(g=2,h=2)
        print(s1 < s2)
        self.assertLessEqual(s1,s2)


    def test_sld(self) :
        s1 = map_state(g = 1,h=1)
        val = sld(s1)
        self.assertLessEqual(val, 14)