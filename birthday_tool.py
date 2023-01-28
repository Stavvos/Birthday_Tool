class Person: 
	
	#Person's attributes
	def __init__ (self, name, day, month):
		self.__name = name
		self.__day = day
		self.__month = month

	#mutator functions 
	def set_name(self,name):
		self.__name = name
	
	def set_day(self, day):
		self.__day = day 
	
	def set_month(self, month):
		self.__month = month
	
	#accessor functions 
	def get_name(self):
		return self.__name
	
	def get_day(self):
		return self.__day 
	
	def get_month(self):
		return self.__month 
	
