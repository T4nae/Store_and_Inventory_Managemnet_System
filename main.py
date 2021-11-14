import csv

#lists and data
cart = list()
cart_total = 0


def list_all(): 
    '''
    displays all the data in the csv file
    '''
    with open('products.csv') as reader_obj:
        csv_reader = csv.reader(reader_obj)
        items = []
        for row in csv_reader:
            items.append(row)
    return items

def list_one(product_name):
    '''
    lists all data for 1 item by its name
    '''
    list = list_all()
    for i in list:
        if i[0] == product_name:
            name = i[0]
            price = int(i[1])            
            stock = int(i[2])
        else:
            pass
    item = [name,price,stock]
    return item

def append_list(list_of_elem):
    '''
    adds new item and row in csv file at the end taking an list as input
    '''
    # Open file in append mode
    with open('products.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def remove_from_list(product_name):
    '''
    removes an nested list from csv file and write the whole file again but without the item which was removed
    '''
    list = list_all()
    list = [i for i in list if i[0] != product_name]
    with open('products.csv', 'w', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerows(list)

def edit_list(product_name, new_name, price, stock):
    '''
    edits an nested list from cv file and write the whole file again but with edited item identified by its name 
    '''
    list = list_all()
    for i in list:
        if i[0] == product_name:
            i[0] = new_name
            i[1] = price
            i[2] = stock
        else:
            pass              
    with open('products.csv', 'w', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerows(list)

def show_cart():
    '''
    shows current items in cart and price
    '''
    print('YOUR CART:: ', cart)
    print('CART TOTAL:: ', cart_total)

def add_cart(product_name):
    '''
    add items to your cart by name and maintains total value of cart
    '''
    global cart_total
    global cart
    list = list_all()
    for i in list:
        if i[0] == product_name:
            if int(i[2]) > 0:
                cart.append(product_name)  
                cart_total += int(i[1])
            else:
                print('not enough stock')     
        else:
            pass

def clear_cart():
    '''
    resets the cart and all the items in it
    '''
    global cart
    global cart_total

    cart.clear()
    cart_total = 0

def checkout():
    '''
    shows summary of your payment and items bougth and updates the stock
    '''
    print("You bought: ",cart)
    print("Total: ","rs",round(cart_total,2))
    tax= round(0.18*cart_total,2)
    print("GST is 18%: ","rs",tax)
    total = round(cart_total+tax,2)
    print("After Tax: ","rs",total)
    print()
    print("Thank you for using The Store")

    for i in cart:
        decrement_stock(i)
    clear_cart()   
      
def decrement_stock(product_name):
    '''
    removes 1 from the stock of product by name and removes the item if no stock is available
    '''
    item = list_one(product_name)
    item[2] -= 1
    edit_list(product_name,item[0],item[1],item[2])

    if item[2] == 0:
        remove_from_list(product_name)

def seller():
    print()
    print('SELECT AN OPTION T0 PROCEED')
    print(40*'---')
    print('A- add an item to sell')
    print('R- remove an item')
    print('E- edit name , price and stock of an item')
    print('O- check data for an item')
    print('L- check all the items in stock')
    print('Q- return')

    c= str()
    while(c != 'Q' or c != 'q'):
        c=input('What would you like to do? ')

        if(c=="q" or c=="Q"):
            selector()
            break
           
        
        elif(c == 'A' or c == 'a'):
            name=input('Enter name of product= ')
            price=int(input('Enter price of product= '))
            stock=int(input('Enter stock available of product= '))
            l = [name,price,stock]
            append_list(l)
            print('product entered in data')
        
        elif(c == 'R' or c == 'r'):
            name=input('Enter name of the product you want to remove= ')
            remove_from_list(name)
            print('product removed')  

        elif(c == 'E' or c == 'e'):
            name=input('Enter name of the product you want to edit= ')
            new_name=input('Enter edited name= ')
            new_price=int(input('Enter edited price= '))
            new_stock=int(input('Enter edited stock ammount= '))
            edit_list(name,new_name,new_price,new_stock)
            print('product edited')
        
        elif(c == 'O' or c == 'o'):
            name=input('Enter name of product= ')
            print(list_one(name))    

        elif(c == 'L' or c == 'l'):
            print(list_all())

def buyer():
    print()
    print('SELECT AN OPTION TO PROCEED')
    print(40*'---')
    print('L- check all items for sale')
    print('O- check data for an item')
    print('S- view items in cart')
    print('A- add item to cart')
    print('C- clear cart')
    print('P- purchase')
    print('Q- return')

    c= str()
    while(c != 'Q' or c != 'q'):
        c=input('What would you like to do? ')

        if(c=="q" or c=="Q"):
            clear_cart()
            selector()
            break

        elif(c == 'L' or c == 'l'):
            print(list_all())

        elif(c == 'O' or c == 'o'):    
            name=input('Enter name of product= ')
            print(list_one(name))

        elif(c == 'S' or c == 's'):
            show_cart()

        elif(c == 'A' or c == 'a'):
            name = input('Enter name of product= ')
            add_cart(name)
            print('CART UPDATED')

        elif(c == 'C' or c == 'c'):  
            clear_cart()
            print('CART CLEARED')

        elif(c == 'P' or c == 'p'):    
            checkout()
    


def selector():
    print(40*'---')
    print('WELCOME TO STORE AND INVENTORY MANAGEMENT SYSTEM')
    print('SELECT AN OPTION TO PROCEED')
    print(40*'---')
    print('1. Seller')
    print('2. Buyer')
    print('3. Quit')

    c= str()
    while(c != 3):
        c=int(input('Enter your choice= '))
            
        if(c== 3):
            print(40*'---')
            print('THANKS FOR USING STORE AND INVENTORY MANAGEMENT SYSTEM')
            print('MADE BY TANYAM BAWEJA and GURNOOR SINGH MAAN CLASS XII N.MED')
            print(40*'---')
            break
        
        elif(c == 2):
            buyer()
            break

        elif(c == 1):
            print('Default username and pass= ADMIN')
            print(40*'---')
            admin=input('Enter username= ')
            passw=input('Enter password= ')
                
            if admin == 'ADMIN' and passw == 'ADMIN':
                seller()
                break
            else:
                print('Wrong pass')
                
selector()                
