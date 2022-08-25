from random import randint as ri

field = [['-', '-', '-'],
	 ['-', '-', '-'],
	 ['-', '-', '-'],]

def print_field():
	print('\n  ¹ ² ³')
	nums = ['¹', '²', '³']
	for i in range(len(field)):
		print(nums[i] , end=' ')
		print(*field[i])



def ask_coords():
	try:
		x, y = input("coordinates (y then x axis): ").split(' ')
	except:
		print('Error: Try write your values a space, e.g.: 1 2')
		x, y = ask_coords()
		return x, y

	x = int(x)
	y = int(y)

	if x > 3 or x < 1 or y > 3 or y < 1:
		print('Error: No value can be bigger than 3 or smaller than 1')
		x, y = ask_coords()
		return x, y


	if type(x) != int or type(y) != int:
		print('Error: both values should be integer')
		x, y = ask_coords()
		return x, y

	x -= 1
	y -= 1

	place_(x, y, 'x')
	return x, y



def place_(x, y, char_):
	if field[x][y] == '-':
		field[x][y] = char_
	else:
		print('Error: This place is taken')



def computer_place():
	empty_list = []

	for i in range(len(field)):
		for j in range(len(field[i])):
			if field[i][j] == '-':
				empty_list.append([i, j])

	if len(empty_list) > 1:
		rand_num = ri(0, len(empty_list)-1)
		x = empty_list[rand_num][0]
		y = empty_list[rand_num][1]
		place_(x, y, 'o')
		countinue_ = True
	else:
		countinue_ = False

	return countinue_



def check_():
	result_h = []
	result_v = []
	result_d1 = []
	result_d2 = []
	win = None

	for i in range(3):
		result_d1.append(field[i][i])
		result_d2.append(field[abs(2-i)][i])

		for j in range(3):
			result_h.append(field[i][j])
			result_v.append(field[j][i])

		if result_h == ['x', 'x', 'x'] or result_v == ['x', 'x', 'x']:
			win = True
		elif result_h == ['o', 'o', 'o'] or result_v == ['o', 'o', 'o']:
			win = False

		if result_d1 == ['x', 'x', 'x'] or result_d2 == ['x', 'x', 'x']:
			win = True
		elif result_d1 == ['o', 'o', 'o'] or result_d2 == ['o', 'o', 'o']:
			win = False

		# print(result)
		result_h, result_v = [], []

	return win




print('====================')
print('    W E L C O M E   ')
print('====================', end='\n\n')


countinue_ = True
win = None
while True:
	if win == True:
		print('\n\nPLAYER WINS!')
		countinue_ = False
	if win == False:
		print('\n\nYOU LOSE!')
		countinue_ = False

	if countinue_ == False:
		print_field()
		break

	print_field()
	x, y = ask_coords()
	countinue_ = computer_place()
	win = check_()




