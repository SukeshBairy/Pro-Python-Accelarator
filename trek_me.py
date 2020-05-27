from tabulate import tabulate
from project_main import Trek
from data import *


customer_details = {}
total_me = 30
print("-" * 30)
print("WELCOME TO WONDER ADVENTURES")
print("-" * 30)
while True:
    choice = int(input("Where do you want to visit?\n\
						1.Upcoming_Treks\n\
						2.Himachal_Treks\n\
						3.Change of number of seats\n\
						4.Contact us\n\
						5.Show Status\n\
						6.EXIT\n-->"))
    if choice == 1:
        sub_choice = int(input("Which place are you looking for?\n\
							  1.Karnataka\n\
							  2.Tamil Nadu\n\
							  3.Kerala\n\
							  4.Maharashtra\n\
							  5.EXIT\n-->"))
        if sub_choice == 1:
            print(tabulate(Karnataka, headers_karnataka_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3,4,5,6)\n-->"))
                place_name -= 1
                for i, j in enumerate(kar):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (kar[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   
        elif sub_choice == 2:
            print(tabulate(Tamil_Nadu, headers_tamilnadu_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(tn):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (tn[j])
                        total_cost=cost*number_of_seats
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   
        elif sub_choice == 3:
            print(tabulate(Kerala, headers_kerala_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(ker):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (ker[j])
                        total_cost=cost*number_of_seats
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   
        elif sub_choice == 4:
            print(tabulate(Maharashtra, headers_maharashtra_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(mah):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (mah[j])
                        total_cost=cost*number_of_seats
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   
        else:
            pass
    elif choice == 2:
        sub_choice = int(input("Which place are you looking for?\n\
							  1.Himachal_Pradesh\n\
							  2.Sikkim\n\
							  3.Uttarkhand\n\
							  4.EXIT\n-->"))
        if sub_choice == 1:
            print(tabulate(Himachal_Pradesh,
                           headers_himachalpradesh_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(h_p):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (h_p[j])
                        total_cost=cost*number_of_seats 
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   
        elif sub_choice == 2:
            print(tabulate(Sikkim, headers_sikkim_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1)\n-->"))
                place_name -= 1
                for i, j in enumerate(si):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (si[j])
                        total_cost=cost*number_of_seats 
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass                   

        elif sub_choice == 3:
            print(tabulate(Uttarkhand, headers_uttarkhand_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(ut):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (ut[j])
                        total_cost=cost*number_of_seats
                        t = Trek(name, email_id, number_of_seats, place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name,place,total_cost)
            elif yes_no == "n":
            	print("Look for another place maybe :D")
            	pass             

        else:
            pass
    elif choice == 3:
        i = input("Enter your email ID:")
        if i in customer_details.keys():
            changed_seats = int(input("How many seats you want to book?\n-->"))
            cost=t.total_cost//t.number_of_seats
            t.update_seats(changed_seats,cost)
            t.congrats(t.name,t.place,t.total_cost)
        else:
        	print("Email ID not found . Please try another ID.")
        	pass    
    elif choice == 4:
        print(tabulate(tables_info, headers_info, tablefmt="orgtbl"))

    elif choice == 5:
        email = input("Enter your email ID:")
        if email  in customer_details.keys():
        	table=[[t.name,t.place,t.total_cost,t.number_of_seats]]
        	header=["Name","Place","Cost","Seats"]
        	print(tabulate(table,header,tablefmt="orgtbl"))
            # print(t.name, "|",       t.place, "|",
            #      "₹",t.total_cost, "|",       t.number_of_seats)
    else:
        print("THANK YOU.VISIT AGAIN.")
        break



