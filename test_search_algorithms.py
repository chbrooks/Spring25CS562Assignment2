from unittest import TestCase
from mars_planner import *
from search_algorithms import *


class Test(TestCase):
    def test_breadth_first_search(self):
        def g(s):
            return s.rover_loc == "battery"
        s = RoverState()
        result = breadth_first_search(s, action_list, g)
        print(result)
        def g2(s):
            return s.rover_loc == "station" and s.sample_loc == "station"
        s2 = RoverState()
        result = breadth_first_search(s2, action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_loc == "station"
        s3 = RoverState()
        result = breadth_first_search(s3, action_list, g3)
        print(result)

    def test_depth_first_search(self):
        def g(s):
            return s.rover_loc == "battery"
        s = RoverState()
        result = depth_first_search(s, action_list, g)
        print(result)
        def g2(s):
            return s.rover_loc == "sample" and s.sample_loc == "station"
        s2 = RoverState()
        result = depth_first_search(s2, action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_extracted == "station"
        s3 = RoverState()
        result = depth_first_search(s3, action_list, g3)
        print(result)
