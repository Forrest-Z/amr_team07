#!/usr/bin/env python

PACKAGE = 'amr_navigation'

#import math
from math import atan2, copysign, sqrt, cos, sin
from velocity_controller import VelocityController, Velocity
from velocity_controller import get_shortest_angle, get_distance

class OmniVelocityController(VelocityController):

    def __init__(self, *args):
        raise NotImplementedError('This is your assignment to implement OmniVelocityController')
        pass


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

    
    def __init__(self, l_max_vel, l_tolerance, a_max_vel, a_tolerance, max_linear_acceleration, max_angular_acceleration):
        self._l_max_vel = l_max_vel
        self._l_tolerance = l_tolerance
        self._a_max_vel = a_max_vel
        self._a_tolerance = a_tolerance
        self._l_accel = max_linear_acceleration
        self._a_accel = max_angular_acceleration

    def compute_velocity(self, actual_pose):



        # Displacement and orientation to the target in world frame:
        dx = self._target_pose.x - actual_pose.x
        dy = self._target_pose.y - actual_pose.y

        # Step 1: compute remaining distances
        linear_dist = get_distance(self._target_pose, actual_pose)
        angular_dist = get_shortest_angle(self._target_pose.theta, actual_pose.theta)
        angular_dist_orientation = get_shortest_angle(atan2(dy, dx), actual_pose.theta)

        #Is target pose reached
        if (    abs(linear_dist)<self._l_tolerance and
                abs(angular_dist)<self._a_tolerance     ):
            self._linear_complete = True
            self._angular_complete = True
            return Velocity()
        
     
        # Step 2: compute velocities wich accelerations
        
        
        linear_vel=self._l_max_vel
        angular_vel=self._a_max_vel

        linear_vel_x=0
        linear_vel_y=0
        matched_angular_vel=0
        matched_linear_vel=0            

        #time needed to accomplish linear and angular motions
        t_for_linear=abs(linear_dist/linear_vel)
        t_for_angular=abs(angular_dist/angular_vel)


        #minimum time to slow down
        t_linear_min=abs(linear_vel/self._l_accel) 
        t_angular_min=abs(angular_vel/self._a_accel)


        #Not needed for comparison
        t_linear_difference = (t_for_linear - t_linear_min)
        t_angular_difference = (t_for_angular - t_angular_min)
        
        a=(t_for_angular/t_for_linear)
        l=(t_for_linear/t_for_angular)

        #Used when close to goal       
        if (t_for_linear<=t_linear_min and t_for_angular<=t_angular_min):
            matched_linear_vel=(linear_vel*l+(self._l_accel*(-1)*(t_for_linear)))
            matched_angular_vel=(angular_vel*a+(self._a_accel*(-1)*(t_for_angular)))

        #Used when motion is only x and y motion is needed
        elif (abs(angular_dist)<0.02):
            matched_linear_vel=(sqrt(abs(((linear_vel)**2+2*self._l_accel*(-1)*linear_dist))))
            matched_angular_vel=0

        #Used when only rotation is needed
        elif (abs(linear_dist)<0.02):
            matched_linear_vel=0
            matched_angular_vel=(sqrt(abs(((angular_vel*a)**2+2*self._a_accel*(-1)*angular_dist))))
        
        #Used in the beginning
        else:           
            matched_linear_vel=(linear_vel*l)#+(self._l_accel*(-1)*(t_for_linear)))
            matched_angular_vel=(angular_vel*a)#+(self._a_accel*(-1)*(t_for_angular)))   

          


        if (abs(linear_dist)>self._l_tolerance):
           
            
            linear_vel_x = (matched_linear_vel*cos(angular_dist_orientation)
                                                            if abs(linear_dist)>self._l_tolerance 
                                                            else self._l_tolerance*cos(angular_dist_orientation))

            linear_vel_y = (matched_linear_vel*sin(angular_dist_orientation)
                                                            if abs(linear_dist)>self._l_tolerance 
                                                            else self._l_tolerance*sin(angular_dist_orientation))
            
            
        if abs(angular_dist)>self._a_tolerance:
            angular_vel = (matched_angular_vel 
                                    if abs(angular_dist)>self._a_tolerance else self._a_tolerance)
        



        return Velocity(copysign(linear_vel_x, dx),
                        copysign(linear_vel_y, dy),
                        copysign(angular_vel, angular_dist))
