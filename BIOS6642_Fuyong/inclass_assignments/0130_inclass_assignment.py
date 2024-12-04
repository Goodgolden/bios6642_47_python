cover_price = float(input('Please provide the price: '))
num = int(input('Please provide the number of books: '))

book_cost = cover_price * num * (1 - 0.4)
shipment_cost = 5 + 0.75 * (num - 1)
total_cost = book_cost + shipment_cost
print('The total cost: $', total_cost, sep='')
