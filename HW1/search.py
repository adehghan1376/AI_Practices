# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    fringe=util.Stack()

    Starting_StateName = problem.getStartState()
    Starting_State=(Starting_StateName , [] , 0)              # State Structure is :(state_name,state_path,state_cost)
                                                               # that we made it
    fringe.push(Starting_State)
    closed=set()                                           # an array --> name of already expanded nodes

    while not fringe.isEmpty():
        (Expanded_StateName,Expanded_StatePath,Expanded_StateCost)= fringe.pop()
        if  Expanded_StateName in closed:
            pass
        else:
            closed.add(Expanded_StateName)
            if(problem.isGoalState(Expanded_StateName)):              # gets a name
                return Expanded_StatePath
            for StateName , StateAction , StateCost in problem.getSuccessors(Expanded_StateName):   # an array of 3 part tuples with data structure like: (near_state_name,packman_action,state_path_cost)
                add_StatePath = Expanded_StatePath + [StateAction]
                add_StateCost = Expanded_StateCost + StateCost
                add_State=(StateName,add_StatePath,add_StateCost)     # translates getSuccessor() output to our state data type
                fringe.push(add_State)


    return ["Error! Can't find the Goal State!"]


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe=util.Queue()


    Starting_StateName = problem.getStartState()
    Starting_State=(Starting_StateName , [] , 0)              # State Structure is :(state_name,state_path,state_cost)
                                                               # that we made it
    fringe.push(Starting_State)
    closed=set()
    SeenNode=set()                                              # an array of seen nodes  in order to avoid duplicate node in fringe

    SeenNode.add(Starting_StateName)



    while not fringe.isEmpty():
        (Expanded_StateName,Expanded_StatePath,Expanded_StateCost)= fringe.pop()
        if  Expanded_StateName in SeenNode:
            if  Expanded_StateName in closed:
               pass
            else:
                closed.add(Expanded_StateName)
                if(problem.isGoalState(Expanded_StateName)):              # gets a name
                    return Expanded_StatePath
                for StateName , StateAction , StateCost in problem.getSuccessors(Expanded_StateName):   # an array of 3 part tuples with data structure like: (near_state_name,packman_action,state_path_cost)
                    add_StatePath = Expanded_StatePath + [StateAction]
                    add_StateCost = Expanded_StateCost + StateCost
                    add_State=(StateName,add_StatePath,add_StateCost)     # translates getSuccessor() output to our state data type
                    fringe.push(add_State)
                    SeenNode.add(StateName)

    return ["Error! Can't find the Goal State!"]

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe=util.PriorityQueue()

    Starting_StateName = problem.getStartState()
    Starting_State=(Starting_StateName , [] , 0)              # State Structure is :(state_name,state_path,state_cost)
                                                               # that we made it
    fringe.push(Starting_State,0)                              # starting_State with priority=0


    SeenNodeCost={}                                             # cost of SeenNode
    closed=set()                                                # an array --> name of already expanded nodes

    SeenNodeCost[Starting_StateName]=0                          # cost of SeenNode--> Starting_StateName at first is 0


    while not fringe.isEmpty():
        (Expanded_StateName,Expanded_StatePath,Expanded_StateCost)= fringe.pop()
        if  Expanded_StateName in closed:
            pass
        else:
            closed.add(Expanded_StateName)
            if(problem.isGoalState(Expanded_StateName)):              # gets a name
                return Expanded_StatePath
            for StateName , StateAction , StateCost in problem.getSuccessors(Expanded_StateName):   # an array of 3 part tuples with data structure like: (near_state_name,packman_action,state_path_cost)
                add_StatePath = Expanded_StatePath + [StateAction]
                add_StateCost = Expanded_StateCost + StateCost
                add_State=(StateName,add_StatePath,add_StateCost)     # translates getSuccessor() output to our state data type
                fringe.push(add_State,add_StateCost)


    return ["Error! Can't find the Goal State!"]

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe=util.PriorityQueue()

    Starting_StateName = problem.getStartState()
    Starting_State=(Starting_StateName , [] , 0)              # State Structure is :(state_name,state_path,state_cost)
                                                               # that we made it


    SeenNodeCost={}                                                              # Dictionary -->cost of SeenNode

    closed=set()                                                             # an array --> name of already expanded nodes

    fringe.push(Starting_State,heuristic(Starting_StateName,problem))                              # starting_State with priority=0

    SeenNodeCost[Starting_StateName]=heuristic(Starting_StateName,problem)                   # cost of SeenNode--> Starting_StateName at first is 0


    while not fringe.isEmpty():
        (Expanded_StateName,Expanded_StatePath,Expanded_StateCost)= fringe.pop()
        if  Expanded_StateName in closed:
            pass

        else:
            closed.add(Expanded_StateName)
            SeenNodeCost[Expanded_StateName]=Expanded_StateCost
            if(problem.isGoalState(Expanded_StateName)):              # gets a name
                return Expanded_StatePath
            for StateName , StateAction , StateCost in problem.getSuccessors(Expanded_StateName):   # an array of 3 part tuples with data structure like: (near_state_name,packman_action,state_path_cost)
                add_StatePath = Expanded_StatePath + [StateAction]
                add_StateCost = Expanded_StateCost + StateCost
                add_State=(StateName,add_StatePath,add_StateCost)     # translates getSuccessor() output to our state data type
                fringe.push(add_State,add_StateCost +  heuristic(StateName,problem))





            """                # for managing the duplication on  seen node cost
            try:             #if seennodecost[startname].isset()
                if SeenNodeCost[StateName]> add_StateCost +  heuristic(StateName,problem):
                    fringe.push(add_State,add_StateCost +  heuristic(StateName,problem))


            except:
                    fringe.push(add_State,add_StateCost +  heuristic(StateName,problem))
                SeenNodeCost[StateName]=add_StateCost +  heuristic(StateName,problem)"""




    return ["Error! Can't find the Goal State!"]


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
