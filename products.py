# While 比較適合用在不知道會重複幾次的迴, 比起for loop

products = []
while True:
	name = input ('product name: ')
	if name == 'q': #q = exit
		break
	price = input ('price: ')
	p = []
	p.append(name)
	p.append (price)
	products.append (p)

print (products)

print (products[0][0]) #大清單的第0格裡面的第0格