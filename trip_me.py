from tabulate import tabulate
from Main_one import TripMe


members={}
customer_id=0


tables_upcoming_treks=[[1,"Karnataka","Kodachadri Trek","4150"],[2,"Karnataka","Tadiandamol Trek, Coorg","3954"],[3,"Karnataka","Kudremukh Trek","4878"],[4,"Karnataka","Kumara Parvatha Trek","4014"],[5,"Karnataka","Dudhsagar Waterfalls Trek","5900"],[6,"Karnataka","Gokarna Beach Trek & Camping","4539"],[7,"Maharashtra","Trek to Plus Valley, Tamhini Ghat","2500"],[8,"Maharashtra","Trek to Alang, Madan and Kulang ( AMK )","3600"],[9,"Maharashtra","Trek to Sandhan Valley","2500"],[10,"Tamil Nadu","Kotagiri Trek, Ooty","4940"],[11,"Tamil Nadu","Trek to Canopy Hills, Vattakanal","5706"],[12,"Tamil Nadu","Top Station Trek - Munnar","4428"],[13,"Kerala","Paithalmala Trek, Kerala","3953"],[14,"Kerala","Trek to Banasura Hills, Wayanad","3600"],[15,"Kerala","Night Trekking & Camping at Wayanad","4600"],["E","X","I","T"]]
headers_upcoming_treks=["sl.no","State","Places","Price"]

tables_himalayan_treks=[[1,"Himachal Pradesh","Trek to Malana - Chandrakhani Pass, Himachal Pradesh","8900"],[2,"Himachal Pradesh","Children's Adventure Camp at Manali - Himalayas","23250"],[3,"Himachal Pradesh","Trek to Hampta Pass and Chandratal - Himalayas","10600"],[4,"Sikkim","Trek to Goechala, Sikkim","15200"],[5,"Uttarkhand","Brahmatal Trek","8800"],[6,"Uttarkhand","Stok Kangri Expedition (6153 m)- Ladakh","9700"],[7,"Uttarkhand","Ladakh Bike Trip","16780"],["E","X","I","T"]]
headers_himalayan_tricks=["sl.no","State","Places","Price"]
#for index,item in enuermate(tables_upcoming_treks):
#	print(index,"-->",item)
print(len(tables_upcoming_treks))
tables_info=[["Enquiry Name","Sukesh Bairy"],["Phone Number","9686853769"],["Email_id","sukeshbairy@gmail.com"],["Address","Puttenahalli, Phase 7, J. P. Nagar, Bengaluru, Karnataka,560078"]]
headers_info=["_Type_","_Info_"]


print("-"*30)
print("WELCOME TO TRIP ME")
print("-"*30)



name = input("Name: ")
ph_no = input("Phone: ")
email_id = input("Enter your Email_id: ")
seats = int(input("How many seats are you looking for: "))
tm=TripMe(name,ph_no,email_id,seats)
customer_id+=1
members[customer_id]=tm
print(customer_id,tm.name,tm.seats)



while True:
	ch=int(input("Enter a choice\n\
		            1.Add more customers\n\
				  2.Upcoming Treks\n\
				  3.Himalayan Treks\n\
				  4.Contact us\n\
				  5.Changes in booking seats?\n\
				  6.Exit\n-->"))
	if ch ==1:
		name = input("Name: ")
		ph_no = input("Phone: ")
		email_id = input("Enter your Email_id: ")
		seats = int(input("How many seats are you looking for: "))
		tm=TripMe(name,ph_no,email_id,seats)
		customer_id+=1
		members[customer_id]=tm
		print(customer_id,tm.name,tm.seats)

	elif ch == 2:
		print(tabulate(tables_upcoming_treks,headers_upcoming_treks,tablefmt="github"))
		places=int(input("where do you like to go?\n-->"))
		for i in range(1,len(tables_upcoming_treks)):
			for j in range(1,i):
				if places == i:
					printf" Congrats {tm.name}!\nYour trip to {tables_upcoming_treks[j][2]} is done.\n Your Trip expenses gonna cost {tables_upcoming_treks[j][3]}.\n For more information , details will be sent to your Email_id {tm.email_id}.")
				else:
					pass	
	elif ch == 3:
		print(tabulate(tables_himalayan_treks,headers_himalayan_tricks,tablefmt="github"))	
		places=int(input("where do you like to go?\n-->"))
		for i in range(1,len(tables_himalayan_treks)):
			for j in range(1,i):
				if places == i:
					print(f"Congrats {tm.name}!\nYour trip to {tables_himalayan_treks[j][2]} is done.\n \n Your Trip expenses gonna cost {tables_himalayan_treks[j][3]}.\n For more information , details will be sent to your Email_id {tm.email_id}.") 
				else:
					pass	
	elif ch == 4:
		print(tabulate(tables_info,headers_info,tablefmt="github"))	
	elif ch == 5:
		pass
	elif ch == 6:
		break		
