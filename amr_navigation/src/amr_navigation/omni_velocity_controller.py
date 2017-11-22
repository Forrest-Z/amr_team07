#!/usr/bin/env python

PACKAGE = 'amr_navigation'

import math
from velocity_controller import VelocityController, Velocity
from velocity_controller import get_shortest_angle, get_distance

class OmniVelocityController(VelocityController):

    def __init__(self, l_max_vel, l_tolerance, a_max_vel, a_tolerance, l_max_acc, a_max_acc):
        self._l_max_vel = l_max_vel
        self._l_tolerance = l_tolerance
        self._a_max_vel = a_max_vel
        self._a_tolerance = a_tolerance
        self._l_max_acc = l_max_acc
        self._a_max_acc = a_max_acc

    def compute_velocity(self, actual_pose):
        # Displacement and orientation to the target in world frame:
        dx = self._target_pose.x - actual_pose.x
        dy = self._target_pose.y - actual_pose.y

        # Step 1: compute remaining distances
        linear_dist = get_distance(self._target_pose, actual_pose)
        angular_dist_1 = get_shortest_angle(self._target_pose.theta, actual_pose.theta)

        if (    abs(linear_dist)<self._l_tolerance and
                abs(angular_dist_1)<self._a_tolerance     ):
            self._linear_complete = True
            self._angular_complete = True
            return Velocity()
            
        # Step 2: compute velocities
        #Initializing the velocities
        x_linear_vel, y_linear_vel, angular_vel = 0, 0, 0

        lin_time = self._l_max_vel / self._l_max_acc
        ang_time = self._a_max_vel / self._a_max_acc

        if (abs(linear_dist)>self._l_tolerance or ((self._target_pose.theta - actual_pose.theta)!=0)) :
            #Getting the orientation of the goal with respect to the current position of the bot
            angular_dist = get_shortest_angle(math.atan2(dy, dx), actual_pose.theta)
            #Resolving the linear velocity vector in the x direction using cosine
            x_linear_vel = (self._l_max_vel*math.cos(angular_dist) if abs(linear_dist)>5*self._l_tolerance else
                          self._l_tolerance)
            #Resolving the linear velocity vector in the y direction using sine
            y_linear_vel = (self._l_max_vel*math.sin(angular_dist) if abs(linear_dist)>5*self._l_tolerance else
                          self._l_tolerance)
            #Angular velocity is divided into a part for every unit of linear distance so that the angular
            #transition is synced with the linear motion
            angular_vel = (angular_dist_1*self._a_max_vel/linear_dist)
            #Publishing the calculated linear and angular velocity using Velocity() class in velocity_controller.py
            return Velocity(x_linear_vel,y_linear_vel,angular_vel)
        else:
            #If the bot has reached the target close enough to breach the tolerance, we simply stop it by giving 0 velocity
            return Velocity(0,0,0)


    """
    ========================= YOUR CODE HERE =========================

    Instructions: put here all the functions that are necessary to
    implement the VelocityController interface. You may
    use the DiffVelocityController as an example.

    Implement the constructor to accept all the necessry parameters
    and implement compute_velocity() method

    You are free to write any helper functions or classes you might
    need.

    ==================================================================

    """
