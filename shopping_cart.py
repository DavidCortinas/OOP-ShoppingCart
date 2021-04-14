from IPython.display import clear_output

shopping_cart = []

done = False

i_num = 1

total = 0.00

def show(a_list):
    for dictionary in a_list:
        print(f"{dictionary['item_num']}. {dictionary['item']} - {dictionary['qty']} - {dictionary['item_price']}ea. = {dictionary['selection_price']} ")
        #dictionary keys: item_num, item, qty, price
    
while not done:
    print("""Type 'show' to see your cart.
Type 'clear' to clear out your cart.
Type 'cancel' to cancel your order.
Type 'pay' to checkout.""")
#     total += sp
    is_shopping = input("Press 'ENTER' to keep shopping.").lower()
    clear_output()

    if is_shopping == 'cancel':
        print("Have a nice day! Goodbye.")
        done = True
    elif is_shopping == 'show':
        show(shopping_cart)
        remove = input("Would you like to remove an item(y/n)? ")
        if remove == 'y':
            remove_item = input("Select the item number for the item that you want to remove. ")
            for i in range(len(shopping_cart)):
                if shopping_cart[i]['item_num'] == int(remove_item):
                    del shopping_cart[i]
        else:
            pass
        
    elif is_shopping == 'clear':
        del shopping_cart[:]
    elif is_shopping == 'pay':
#         total = str(total)
        show(shopping_cart)
        print("Your total is $" + str(total))
        done = True
    else:
        #Accept input to build shopping list
        i = input("What item would you like to add to your cart? ")
        q = input("How many " + i + "(s) would you like to add to your cart? ")
        ip = input("Enter the price of " + i + " in dollars to calculate your total at the end. ")
        sp = float(ip) * float(q)
        #build the dictionary based on inputs
        selection = {
            'item_num': i_num,
            'item': i.lower(),
            'qty': q,
            'item_price': float(ip),
            'selection_price': float(sp),
        }
        
        shopping_cart.append(selection)
    total += sp
    i_num += 1