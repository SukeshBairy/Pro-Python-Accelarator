class Trek:
    
	total=30

	def __init__(self,name,email_id,number_of_seats,place,cost):
		self.name=name
		self.email_id=email_id
		self.number_of_seats=number_of_seats
		self.place=place
		self.cost=cost


	def update_seats(self,changed_seats):
		self.number_of_seats=changed_seats	


