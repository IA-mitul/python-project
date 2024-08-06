class resturant:
    menu=dict()
    order_list=list()
    def __init__(self): #constructor
        self.menu={
            "Pizza":"500 TK",
            "Burger":"150 TK",
            "Pasta":"100 TK",
            "Cold drinks":"70 TK",
            "Pestry":"50 TK",

        }
    def print_menu(self): #for displaying the menu
        print("Here is the menu ")
        # keys_list=self.menu.keys()
        # items_list=self.menu.items()
        for keys,valus in self.menu.items():
            print(f"\t{keys} : {valus}")


    def order(self): # for taking the order

        order_request=True

        while(order_request):
            
            order_item=input("What would you like to order : ").lower().capitalize()
            if(order_item not in self.menu):
                print("\tSorry.\nItem is not in the menu.\n\tTry something else.")
            else:
                self.order_list.append(order_item)
                again=input("Do you want anything else? ").lower().capitalize()
                if(again!="Yes"):
                    print("Thanks for your order.")
                    order_request=False

    def bill(self): # counting the total bill and stors the data in a text file
        
        total:int=0

        for key in self.order_list:
            price,curency=self.menu[key].split()
            price=int(price)
            total+=price

        print(f"\tYour total bill is {total}\nPlease come again.")

        with open("resturant.txt","w") as f1:
            for key in self.order_list:
                f1.write(f"{key},")
            f1.write(f"\n\ttotal : {str(total)} TK.\n")

    
c1=resturant()
c1.print_menu()
c1.order()
c1.bill()




