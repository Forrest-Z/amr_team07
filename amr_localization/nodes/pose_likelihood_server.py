#!/usr/bin/env python

PACKAGE = 'amr_localization'
NODE = 'pose_likelihood_server'

import roslib
roslib.load_manifest(PACKAGE)
import rospy
import tf
import numpy as np
import math

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped, Pose2D
from amr_srvs.srv import GetMultiplePoseLikelihood, GetMultiplePoseLikelihoodResponse, GetNearestOccupiedPointOnBeam, GetNearestOccupiedPointOnBeamRequest, SwitchRanger


class PoseLikelihoodServerNode:
	"""
	This is a port of the AMR Python PoseLikelihoodServerNode
	"""
	def __init__(self):

		rospy.init_node(NODE)
		# Wait until SwitchRanger service (and hence stage node) becomes available.
		rospy.loginfo('Waiting for the /switch_ranger service to be advertised...');
		rospy.wait_for_service('/switch_ranger')
		try:
			switch_ranger = rospy.ServiceProxy('/switch_ranger', SwitchRanger)
			# Make sure that the hokuyo laser is available and enable them (aka switch on range scanner)
			switch_ranger('scan_front', True)
		except rospy.ServiceException, e:
			rospy.logerror("Service call failed: %s"%e)

		"""
			Expose GetMultiplePoseLikelihood Service here,
			subscribe for /scan_front,
			create client for /occupancy_query_server/get_nearest_occupied_point_on_beam service

			http://wiki.ros.org/ROS/Tutorials/WritingServiceClient(python)
		"""

		self._tf = tf.TransformListener()
		rospy.loginfo('Started [pose_likelihood_server] node.')

		self.scanner_subs = rospy.Subscriber("/scan_front", LaserScan, self.scan_cb, queue_size = 50)

		s = rospy.Service('/pose_likelihood_server/get_pose_likelihood', GetMultiplePoseLikelihood, self.pose_cb)
		rospy.wait_for_service('/occupancy_query_server/get_nearest_occupied_point_on_beam')
		# cresting a client to simulate the poses and give predicted readings
		self.p_client = rospy.ServiceProxy('/occupancy_query_server/get_nearest_occupied_point_on_beam', GetNearestOccupiedPointOnBeam)

	def pose_cb(self, req):
		all_poses = req.poses
		# initializing the likelihood list with zeros initially and updating only when
		# the matches are good between the real values and simulated values
		likelihood_list = list(np.zeros(len(all_poses)))
		# iterating through each pose and calculating the likelihood values
		for p, pose in enumerate(all_poses):
			# initializing the values and counters
			# the values are chosen by trial and error while trying to achieve the best plot possible
			sigma = 0.5
			bad_matches = 0
			acceptable_matches = 0
			total_weight = 1
			# converting the poses in robots team
			beamposes = self.transform_poses(pose)
			# getting the simulated readings/ranges
			service_request = GetNearestOccupiedPointOnBeamRequest()
			service_request.threshold = 5
			service_request.beams = beamposes
			distances = self.p_client(service_request)

			for i in range(len(distances.distances)):
				# real reading
				real_distance = self.real_ranges[i]
				# predicted reading
				pred_range = self.clamp(distances.distances[i], self.range_min, self.range_max)
				# calculating the likelihood only if the predicted range and real range differ by a small amount
				if (abs(real_distance - pred_range) <= 1.6*sigma):
					# calculating the weights for each pose
					individual_weight = np.exp(-(np.power((real_distance - pred_range),2.0) / (2.0*np.power(sigma,2))) \
					                     / (sigma * np.sqrt(2*np.pi)))
					total_weight = total_weight * individual_weight
					acceptable_matches = acceptable_matches + 1
				else:
					bad_matches = bad_matches + 1
			# update the weight only if the number of bad matches is less than the acceptable number
			if bad_matches < 5:
				likelihood_list[p] = total_weight

		likelihood_response = GetMultiplePoseLikelihoodResponse(likelihood_list)
		return likelihood_response

	def scan_cb(self,data):
		# reading in the requirred values from the scanner, including the real distances
		self.number_of_beams = len(data.ranges)
		self.angle_min = data.angle_min
		self.angle_increment = data.angle_increment
		self.real_ranges = list(data.ranges)
		self.range_max = data.range_max
		self.range_min = data.range_min

	def clamp(self, distance, range_min, range_max):
		# function to clamp the predicted distance within the required range
		if distance > range_max:
			return range_max
		elif distance < range_min:
			return range_min
		else:
			return distance

	def transform_poses(self,base_pose):
		# function to transform the pose from robot base to the laser base
		transformed_beams = []
		time = self._tf.getLatestCommonTime("/base_link","/base_laser_front_link")
		position, quaternion = self._tf.lookupTransform("/base_link","/base_laser_front_link",time)
		yaw = tf.transformations.euler_from_quaternion(quaternion)[2]
		x, y, yaw = position[0], position[1], yaw

		# iterating over every pose
		for i in range(len(self.real_ranges)):
			t_pose = Pose2D()
			euler_form = tf.transformations.euler_from_quaternion((base_pose.pose.orientation.x, \
			             base_pose.pose.orientation.y,base_pose.pose.orientation.z,base_pose.pose.orientation.w))
			# shifting the x and y coordinates
			t_pose.x = base_pose.pose.position.x + x
			t_pose.y = base_pose.pose.position.y + y
			# pose of laser beam is the addition of robot's orientation, beam angle, and the yaw
			t_pose.theta = self.angle_min + (i*self.angle_increment) + yaw + euler_form[2]
			transformed_beams.append(t_pose)
		return transformed_beams


	"""
	============================== YOUR CODE HERE ==============================
	Instructions:   implemenent the pose likelihood server node including a
					constructor which should create all needed servers, clients,
					and subscribers, and appropriate callback functions.
					GetNearestOccupiedPointOnBeam service allows to query
					multiple beams in one service request. Use this feature to
					simulate all the laser beams with one service call, otherwise
					the time spent on communication with the server will be too
					long.

	Hint: refer to the sources of the previous assignments or to the ROS
		  tutorials to see examples of how to create servers, clients, and
		  subscribers.

	Hint: in the laser callback it is enough to just store the incoming laser
		  readings in a class member variable so that they could be accessed
		  later while processing a service request.

	Hint: the GetNearestOccupiedPointOnBeam service may return arbitrary large
		  distance, do not forget to clamp it to [0..range_max] interval.


	Look at the tf library capabilities, you might need it to find transform
	from the /base_link to /base_laser_front_link.
	Here's an example how to use the transform lookup:

		time = self._tf.getLatestCommonTime(frame_id, other_frame_id)
		position, quaternion = self._tf.lookupTransform(frame_id,
														other_frame_id,
														time)
		yaw = tf.transformations.euler_from_quaternion(quaternion)[2]
		x, y, yaw = position[0], position[1], yaw

	You might need other functions for transforming routine, you can find
	a brief api description
	http://mirror.umd.edu/roswiki/doc/diamondback/api/tf/html/python/tf_python.html
	"""


if __name__ == '__main__':
	w = PoseLikelihoodServerNode()
	rospy.spin()
