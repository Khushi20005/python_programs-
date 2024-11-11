#Easy Level (Shopping List): You have a list of items you want to buy from the market:
#['apple', 'banana', 'milk', 'bread', 'eggs']. Write a program that adds
#'chocolate' to the end of your shopping list and removes 'milk'. Finally, print the updated
#shopping list.
shopping_list = ['apple', 'banana', 'milk', 'bread', 'eggs']
shopping_list.append('chocolate')
shopping_list.remove('milk')
print("Updated shopping list:", shopping_list)