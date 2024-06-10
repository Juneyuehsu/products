# While 比較適合用在不知道會重複幾次的迴, 比起for loop

#讀取檔案, 用到split 
products = []
with open ('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'product, price' in line:
			continue #繼續跳到下一回, 沒有離開迴圈. (如果用break, 即離開迴圈)
		name, price = line.strip().split (',') #先去掉換行, 用逗點當作切檔
		products.append([name, price])
print (products)

#user input
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

#print (products[0][0]) #大清單的第0格裡面的第0格
for p in products:
	print (p[0],'price is', p[1])

# 把檔案存入
with open ('products.csv', 'w', encoding='utf-8') as f:
	f.write('product, price \n')
	for p in products:
		f.write (p[0] + ',' + p[1] + '\n') # --> 4 個字串合在一個大字串, 丟給f.write