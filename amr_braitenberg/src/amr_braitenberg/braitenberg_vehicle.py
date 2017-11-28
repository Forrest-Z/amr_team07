#!/usr/bin/env python


class BraitenbergVehicle:
<<<<<<< HEAD
	
	TYPE_A = 0  # direct connections
	TYPE_B = 1  # cross connections
	TYPE_C = 2  # direct and cross connections
		
	def __init__(self, *args):
		"""
		init with default params (type A, factor 1.0)
		"""
		self.set_params()
		pass
	
	
	def set_params(self, vehicle_type=TYPE_A, factor_1=1.0, factor_2=1.0):
		self._vehicle_type = vehicle_type
		self._f_1, self._f_2 = factor_1, factor_2
	
	
	def compute_wheel_speeds(self, left_in, right_in):
		"""
		==================== YOUR CODE HERE ====================
		Instructions: based on the input from the left and
					  right sonars compute the speeds of the
					  wheels. Use the parameters stored in the
					  private fields self._vehicle_type, self._f_1, and
					  self._f_2 (if applicable).

		Hint: a good idea would be to pass here the normalized sonar
		readings scaled by maximum range, i.e. proximity to an obstacle
		(in interval [0..1])
		========================================================
		"""
		#Defining speeds according to three braitenberg vehicle types
		if(self._vehicle_type == 0):
			return (left_in*self._f_1, right_in*self._f_1)
		elif(self._vehicle_type == 1):
			return (right_in*self._f_1, left_in*self._f_1)
		elif(self._vehicle_type == 2):
			return ((right_in*self._f_1 + left_in*self._f_2), (right_in*self._f_2 + left_in*self._f_1))



		return (0.0, 0.0)
=======
    
    TYPE_A = 0  # direct connections
    TYPE_B = 1  # cross connections
    TYPE_C = 2  # direct and cross connections
        
    def __init__(self, *args):
        """
        init with default params (type A, factor 1.0)
        """
        self.set_params()
        pass
    
    
    def set_params(self, vehicle_type=TYPE_A, factor_1=1.0, factor_2=1.0):
        self._vehicle_type = vehicle_type
        self._f_1, self._f_2 = factor_1, factor_2
    
    
    def compute_wheel_speeds(self, left_in, right_in):
        """
        ==================== YOUR CODE HERE ====================
        Instructions: based on the input from the left and
                      right sonars compute the speeds of the
                      wheels. Use the parameters stored in the
                      private fields self._vehicle_type, self._f_1, and
                      self._f_2 (if applicable).

        Hint: a good idea would be to pass here the normalized sonar
        readings scaled by maximum range, i.e. proximity to an obstacle
        (in interval [0..1])
        ========================================================
        """



        return (0.0, 0.0)
>>>>>>> 200a7975fe20c1cfce8f1c856f5d5430b60db789
