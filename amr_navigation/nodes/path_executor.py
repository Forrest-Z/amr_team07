#!/usr/bin/env python

PACKAGE = 'amr_navigation'
NODE = 'path_executor'

import roslib
roslib.load_manifest(PACKAGE)
import rospy

from actionlib import SimpleActionClient, SimpleActionServer
from nav_msgs.msg import Path
from amr_msgs.msg import MoveToAction, MoveToGoal, ExecutePathAction, \
                         ExecutePathFeedback, ExecutePathResult, ExecutePathGoal


class PathExecutor:
    _feedback = ExecutePathFeedback()
    _result = ExecutePathResult()

    def __init__(self, name):
        # self._goal_publisher = Simple
        # self.pe_client_for_bug2= SimpleActionClient('/bug2/move_to',MoveToAction)
        # self.pe_client_for_bug2.wait_for_server()

        # self.pe_client_for_bug2= SimpleActionClient('/bug2/move_to',MoveToAction)
        # self.pe_client_for_bug2.wait_for_server()
        # goal_one = MoveToGoal()
        # goal_one.target_pose.pose.position.x = goal.path.poses[2].pose.position.x
        # goal_one.target_pose.pose.position.y = goal.path.poses[2].pose.position.y
        # goal_one.target_pose.pose.orientation.z = goal.path.poses[2].pose.orientation.z
        # self.pe_client_for_bug2.send_goal(goal_one, done_cb = self.move_to_done_cb)


        print "----------------- in __INIT__ ---------------------------------------"
        rospy.loginfo("Creating an action server")
        # Creating a client to perform the bug2 function
        self._move_to_client = SimpleActionClient('/bug2/move_to', MoveToAction)
        # Creating an action server
        self._as = SimpleActionServer('/path_executor/execute_path', ExecutePathAction, \
                                        execute_cb=self.execute_cb, auto_start=False)
        # Starting the server
        self._as.start()
        # Using a flag to aid preemption
        self.flag = True
        # Using a flag to detect the completion of 3 goals
        self.success = True

    def execute_cb(self, goal):
        # Executed every time a goal is sent by the client
        self._move_to_client.wait_for_server()
        # printing the goals in the terminal
    	rospy.loginfo(goal.path.poses)
        # Creating an instance of MoveToGoal to compose a goal message
    	self.move = MoveToGoal()
        # Iterating through the goals and sending it to the move_to_client
    	for i in range(len(goal.path.poses)):
            if i == 2:
                self.success = True
            else:
                self.success = False
    	    self._pose = goal.path.poses[i]
            self.move.target_pose = self._pose
            self._move_to_client.send_goal(self.move, done_cb=self.move_to_done_cb)
            self._move_to_client.wait_for_result()
        # self.success = True
    	rospy.spin()

        # setting the server's preempted() function if it's requested
    	while self.flag :
    		if self._as.is_preempt_requested():
    			rospy.loginfo('%s: Preempted' % self._action_name)
    			self._as.set_preempted()
    			break

    def move_to_done_cb(self, state, result):
    	if(state == 3):
            # Appending the boolean results to the visited and feedback lists
            self._result.visited.append(True)
            self._feedback.reached = True
            self._feedback.pose = self._pose
        elif(state == 4):
    		self._feedback.reached = False
        # Publishing the feedback and result to the screen
    	rospy.loginfo(self._result)
    	self._as.publish_feedback(self._feedback)
    	if self.success == True:
            # Checking the flag for the completion of the tasks and ending the program
            print "All goals are considered"
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node(NODE)
    pe = PathExecutor(rospy.get_name())
    rospy.spin()
