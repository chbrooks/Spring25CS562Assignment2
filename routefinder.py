from queue import PriorityQueue


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    ## location and "x,y" string
    ## mars_graph. A Graph object that tells us which squares on
    ## the map are adjacent.
    ## prev_state: a pointer back to the previous state.
    ## When we reach the goal, we'll follow that back to the start
    ## to generate the sequence of moves.
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'

    ## You implement this.
    ## For the current state:
    ## Use the mars_graph to find all neighbors.
    # Each successor state's g is this state's g + 1.
    #
    def successors(self):
        pass


## You implement A* here. Use BFS and DFS as a starting point.
def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    pass

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    pass
