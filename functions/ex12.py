food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(food_stuff, removed):
    food_stuff.remove(removed)
    return food_stuff
print(remove_item(food_stuff, 'Mango'))
