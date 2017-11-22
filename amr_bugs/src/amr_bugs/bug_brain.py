#!/usr/bin/env python
from planar import Point, Vec2
from planar.c import Line
from math import *

#=============================== YOUR CODE HERE ===============================
# Instructions: complete the currently empty BugBrain class. A new instance of
#               this class will be created for each new move_to command. The
#               constructor receives the goal specification and the mode of
#               wallfollowing (left (0) or right (1)) that is currently in use.
#               All the remaining functions receive the current position and
#               orientation of the robot.
#
# Hint: you can create a class member variable at any place in your code (not
#       only in __init__) by assigning a value to it, e.g.:
#
#           self.some_member_variable = 2012
#
# Hint: you could use the 'planar' library to avoid implementing geometrical
#       functions that check the distance between a point and a line, or any
#       other helper functions that you need. To use its classes add the
#       following import statements on top of the file:
#
#            from planar import Point, Vec2
#            from planar.c import Line
#            from math import degrees
#
#       As discussed in the lab class, you will need to install the library by
#       executing `sudo pip install planar` in the terminal.
#
# Hint: all the member variables whose names start with 'wp_' (which stands for
#       'waypoint') will be automagically visualized in RViz as points of
#       different colors. Similarly, all the member variables whose names
#       start with 'ln_' (which stands for 'line') will be visualized as lines
#       in RViz. The only restriction is that the objects stored in these
#       variables should indeed be points and lines.
#       The valid points are:
#
#           self.wp_one = (1, 2)
#           self.wp_two = [1, 2]
#           self.wp_three = Point(x, y) # if you are using 'planar'
#
#       The valid lines are (assuming that p1 and p2 are valid points):
#
#           self.ln_one = (p1, p2)
#           self.ln_two = [p1, p2]
#           self.ln_three = Line.from_points([p1, p2]) # if you are using 'planar'

class BugBrain:

    TOLERANCE = 0.3

    def __init__(self, goal_x, goal_y, side):
        #storing the initial values
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.side = side
        #to store the values of the point where we leave the wall
        self.leave_x = None
        self.leave_y = None
        self.angle_vec = None
        # to store the distance of the current wall hitting point from goal
        self.last_hit_dist = None
        # to store the distance of the current point from goal
        self.current_to_leave_dist = None
        #storing the values of points while following
        self.hit_list = []
        #storing the values of points where we leave the wall
        self.leaving_points = []
        #to store the point where we hit the wall as a Point
        self.vector_hit = None
        #list to store the leaving points
        self.wp_wall_leave_points = None
        #making a point of the goal and displaying it in Rviz
        self.wp_goal_point = Point(self.goal_x, self.goal_y)
        #count to be used when checking for goal_unreachable
        self.count = 0
        #flag to see whether we've left the wall earlier
        self.flag = False

    def follow_wall(self, x, y, theta):
        """
        This function is called when the state machine enters the wallfollower
        state.
        """
        #storing the values
        self.x = x
        self.y = y
        self.theta = theta
        #making a Point out of it
        self.wp_hit_point = Point(x, y)
        #appending the points to a list
        self.hit_list.append((x,y))
        #making a line from starting point to goal
        self.ln_line_to_goal = Line.from_points([self.wp_hit_point, self.wp_goal_point])
        self.vector_hit = Point(x,y)
        self.angle_vec = self.wp_goal_point-self.vector_hit
        self.last_hit_dist = self.vector_hit.distance_to(self.wp_goal_point)
        #increasing the counter every time follow wall is called
        self.count = self.count + 1

    def leave_wall(self, x, y, theta):
        """
        This function is called when the state machine leaves the wallfollower
        state.
        """
        #setting the flag so that we know we've left the wall once
        self.flag  = True
        #storing the points in a list
        self.wp_wall_leave_points = Point(x,y)

    def is_goal_unreachable(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether the goal is unreachable.
        """
        #storing the values
        self.x_unreach = x
        self.y_unreach = y
        #making a Point out of it
        self.wp_current_pos = Point(x,y)
        self.wp_hit_point.distance_to(self.wp_current_pos)
        # if (self.flag == False):
        #     if(abs(self.wp_hit_point.distance_to(self.wp_current_pos))-abs(self.wp_goal_point.distance_to(self.wp_current_pos)) < 0.3):
        #         return True
        return False

    def is_time_to_leave_wall(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether it is the right time (or place) to
        leave the wall and move straight to the goal.
        """
        #storing the values
        self.leave_x = x
        self.leave_y = y
        self.theta = theta
        #making a vector out of it
        v1 = Vec2(x,y)
        goal_vec = self.wp_goal_point
        #taking the difference between the current vector and the goal vector
        vector3 = v1 - goal_vec
        angles_diff = vector3.angle_to(self.angle_vec)
        #taking the distance from the current point to goal
        self.current_to_leave_dist = v1.distance_to(goal_vec)
        if (abs(self.x - self.leave_x)>0.5 or abs(self.y - self.leave_y)>0.5) and \
        (abs(angles_diff) < 3 or (abs(angles_diff)>176 and abs(angles_diff)<184)):
            self.leaving_points.append((self.leave_x,self.leave_y))
            #if we are closer to goal than the start position, leave wall
            if self.current_to_leave_dist < self.last_hit_dist:
                return True
        return False



#==============================================================================
