from datetime import datetime

name = input("enter your name:")

lists = """
code:[10]-Rice     Rs 20/kg 
code:[11]-Suger    Rs 30/kg 
code:[12]-salt     Rs 20/kg
code:[13]-oil      Rs 80/liter
code:[14]-paneer   Rs 110/kg 
code:[15]-maggi    Rs 50/kg
code:[16]-Boost    Rs 90/kg
code:[17]-colgate  Rs 85/each

This codes Are sample QR codes
"""


#declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0 
items_list=[]
quantity_list = []
price_list=[]

# codes and rates for items
# items ={'Rice':20,'Sugar':30,'salt':20,"oil":80,"paneer":110,"maggi":50,"Boost":90,"colgate":85}

items ={10:{'Rice   ':20},11:{'Sugar  ':30},12:{'salt   ':20},13:{"oil    ":80},14:{"paneer ":110},15:{"maggi ":50},16:{"Boost  ":90},17:{"colgate":85}}
option =int(input("for list of items press 1:"))
if option == 1:
    print(lists)

for i in range (len(items)): # range 8
    inp1 = int(input("if you want to buy press 1 or 0 for exit:"))
    if inp1 == 0:
        break
    if inp1 ==1:
        item =int(input("enter your items code:")) # it takes the item code
        quantity =int(input("enter quantity:")) # it takes the quantity of the item
        if item in items.keys(): 
            
            price =quantity*(items[item][list(items[item].keys())[0]]) 
            # (items[item][list(items[item].keys())[0]]) This is for each item price
            
            pricelist.append((item,quantity,items,price))
            totalprice += price
            items_list.append((list(items[item].keys())[0]))
            quantity_list.append(quantity)
            price_list.append(price)
            gst =(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:")
    if inp == "yes":
        pass
        if finalamount !=0:
            print(26*"=","shankar super market",26*"=")
            print(31*"=","rajamandry",31*"=")
            print("name:",name,29*" ","Date:",datetime.now())
            print(75*'-')
            print("sno",14*" ",'items',14*" ",'Quantity',14*" ",'price')
            print(" ")
            for i in range(len(pricelist)):
                print(i+1,16*" ",items_list[i],15*" ",quantity_list[i],20*" ",price_list[i])
            print(75*"-")
            print(50*" ","TotalAmount:",'Rs',totalprice)
            print('gst Amount:',51*' ','Rs',gst)
            print(75*"-")
            print(50*' ',"finalamount:","RS",finalamount)
            print(75*"-")
            print("Thanks for visiting")
            print(75*"-")








