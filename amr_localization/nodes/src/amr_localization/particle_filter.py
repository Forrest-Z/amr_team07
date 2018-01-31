#!/usr/bin/env python

PACKAGE = 'amr_localization'
NODE = 'particle_filter'

import roslib
roslib.load_manifest(PACKAGE)
import rospy
import math
import random
import numpy as np
from amr_localization import *
from amr_localization.motion_model import MotionModel
from amr_localization.pose import Pose
from amr_localization.particle import Particle
from amr_localization.random_particle_generator import RandomParticleGenerator

class ParticleFilter:

    def __init__(self, map_min_x, map_max_x, map_min_y, map_max_y, weigh_particles_callback):
        self.weigh_particles_callback = weigh_particles_callback
        self.particle_set_size = 100
        self.random_particles_size = 25
        self.motion_model = MotionModel(0.02, 0.01)
        self.random_particle_generator = RandomParticleGenerator(map_min_x, map_max_x, map_min_y, map_max_y)
        self.pose_estimate = Pose()

        self.particles = []
        for i in range(self.particle_set_size):
            self.particles.append(self.random_particle_generator.generate_particle())


    def update(self, x, y, yaw):
        # giving motion update to particles
        self.motion_model.setMotion(x,y,yaw)
        for particle in self.particles:
            particle.pose = self.motion_model.sample(particle.pose)

        # getting the weights of all particles and setting them to each particle
        weights = self.weigh_particles_callback(self.particles)
        for i,particle in enumerate(self.particles):
            particle.weight = weights[i]

        # sorting the particles according to their weights
        self.particles = sorted(self.particles)[::-1]

        # sampling the particles
        cumulative_weights = []
        total = 0.0
        for w in [i/np.sum(weights) for i in weights]:
            total += w
            cumulative_weights.append(total)

        sample_indices = []
        for i in range(self.particle_set_size - self.random_particles_size):
            a = np.random.rand()
            for j,w in enumerate(cumulative_weights):
                if w > a:
                    sample_indices.append(j)
                    break

        self.particles = [self.particles[i] for i in sample_indices]

        # adding 10 random particles to help in kidnapped robot problem
        for i in range(self.random_particles_size):
            self.particles.append(self.random_particle_generator.generate_particle())

        # setting up the best pose estimate
        self.pose_estimate = self.particles[0].pose

        '''
        ============================== YOUR CODE HERE ==============================
         Instructions: do one complete update of the particle filter. It should
                       generate new particle set based on the given motion
                       parameters and the old particle set, compute the weights of
                       the particles, resample the set, and update the private
                       member field that holds the current best pose estimate
                       (self.pose_estimate). Note that the motion parameters provided
                       to this function are in robot's reference frame.

         Hint: Check motion_model.py for documentation and example how to use it
               for the particle pose update.
               x, y, yaw -- are the odometry update of the robot's pose (increments)


         Remark: to compute the weight of particles, use the weigh_particles_callback member
                 field:

                     weights = self.weigh_particles_callback(particles_list)

         Remark: to generate a comletely random particle use the provided
                 random_particle_generator object:

                     particle = self.random_particle_generator.generate_particle()

         Finally  the best pose estimate and assign it to the corresponding member field
         for visualization:
                     self.pose_estimate = selected_particle.pose
        ============================================================================
        '''


    def get_particles(self):
        return self.particles

    def get_pose_estimate(self):
        return self.pose_estimate

    def set_external_pose_estimate(self, pose):
        self.random_particle_generator.set_bias(pose, 0.5, 500)
