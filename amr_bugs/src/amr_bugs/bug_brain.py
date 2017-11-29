#!/usr/bin/env python


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
from planar import Point, Vec2
from planar.c import Line
import rospy


class BugBrain:

    TOLERANCE = 0.3

    def __init__(self, goal_x, goal_y, side):

        self.wp_goal=Vec2(goal_x,goal_y)
        self.obstacle_starting_points=[]
        self.obstacle_ending_points=[]
        self.time = rospy.get_rostime()


    def follow_wall(self, x, y, theta):
        """
        This function is called when the state machine enters the wallfollower
        state.
        """
        #checking whetre new point is already in the list if not add it
        self.wp_obstacle_start=Vec2(x,y)
        is_following=True

        for x in range(len(self.obstacle_starting_points)):
            wp_new_point=self.obstacle_starting_points[x][0]
            if abs(wp_new_point.distance_to( self.wp_obstacle_start)<=1):
                is_following=False

        if (is_following==True) :
            self.obstacle_starting_points.append((self.wp_obstacle_start,0))

        self.time = rospy.get_rostime()

        #line for checking the position
        if len(self.obstacle_ending_points)<1:
            self.ln_line_to_goal=Line.from_points([self.wp_obstacle_start, self.wp_goal])

        pass

    def leave_wall(self, x, y, theta):
        """
        This function is called when the state machine leaves the wallfollower
        state.
        """
        # compute and store necessary variables

        #self.wp_end_obstacle=Vec2(x,y)
        pass

    def is_goal_unreachable(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether the goal is unreachable.
        """
        self.current_position=Vec2(x,y)
        #time is needed as same points are written repeatedly
        next_time = rospy.get_rostime()
        time_diff=abs(self.time.secs-next_time.secs)

        #cheking if goal is reachable after it goes aroung trice
        for x in range(len(self.obstacle_starting_points)):
            wp_new_point=self.obstacle_starting_points[x][0]
            if abs(time_diff>20 and wp_new_point.distance_to(self.current_position)<=self.TOLERANCE):
                self.time = rospy.get_rostime()
                self.obstacle_starting_points[x]=(self.obstacle_starting_points[x][0],self.obstacle_starting_points[x][1]+1)
                if (self.obstacle_starting_points[x][1]>2):
                    return True


        return False

    def is_time_to_leave_wall(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether it is the right time (or place) to
        leave the wall and move straight to the goal.
        """

        self.wp_current_position=Vec2(x,y)

        #check path hasnt been taken earlier if so keep following the wall or leave wall otherwise
        if (abs(self.ln_line_to_goal.distance_to(self.wp_current_position))<=self.TOLERANCE and
                    abs(self.wp_current_position.distance_to(self.wp_obstacle_start))>1):
            is_following=True

            for x in range(len(self.obstacle_ending_points)):
                wp_new_point=self.obstacle_ending_points[x]
                if (abs(wp_new_point.distance_to(self.wp_current_position))<=1):
                    is_following=False
                    break

            if(is_following==True):
                self.obstacle_ending_points.append(self.wp_current_position)
                return True

        return False
