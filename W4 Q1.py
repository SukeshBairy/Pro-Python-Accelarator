class Parking:
    def _init_(self,name,ph,veh_num,types,slot):
        self.name=name
        self.ph=ph
        self.veh_num=veh_num
        self.types=types
        self.slot=slot
dict2={}
dict4={}
c2=5
c4=5    
list2=[0 for i in range(5)]
list4=[0 for i in range(5)]
while(True):    
    ch=int(input("Enter choice:\n1.Park vehicle\n2.Remove vehicle\n3.Exit\n"))
    w=input("a. 2-wheeler\nb. 4-wheeler:\n")
    if ch==1:
        name=input("Enter name:")
        ph=int(input("Enter ph no: "))
        veh_num=input("Enter vehicle number:\n")
        #starttime
        if w=='a':
            types=2
            if c2!=0:
                for i in range(0,len(list2)):
                    if list2[i]==0:
                        list2[i]=1
                        c2=c2-1
                        slot=i+1
                        print(list2)
                        break
                dict2[veh_num]=slot
                print(dict2)
            else:
                print("slot unavailable")
        elif w=='b':
            types=4
            if c4!=0:
                for i in range(0,len(list2)):
                    if list4[i]==0:
                        list4[i]=1
                        c4=c4-1
                        slot=i+1 
                        break
                dict4[veh_num]=slot
            else:
                print("slot unavailable")
        else:
            print("invalid")
            
        p=Parking(name,ph,veh_num,types,slot)
        a={p.name,p.ph,p.veh_num,p.types,p.slot}
        print("your details:\n",p.name,"\n",p.ph,"\n",p.veh_num,"\n",p.types,"\n")
        print("ur slot number:",p.slot)
    
    elif ch==2:
        veh_num1=input("Enter ur vehicle number: ")
        if(w=='a'):
            slot1=dict2[veh_num1]
            c2=c2+1
            list2[slot1-1]=0
            print(list2)
        elif(w=='b'):
            slot1=dict4[veh_num1]
            c4=c4+1
            list4[slot1-1]=0
    else:
        exit(0)