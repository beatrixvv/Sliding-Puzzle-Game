import random

# Take the input of the dimension of the puzzle
# Return the dimension value (integer)
def take_dimension_input():
	while True:
		try:
			dimension = int(input('Enter the dimension (3-10): '))
			if dimension < 3 or dimension > 10:
				print('Enter an integer between 3 and 10')
			else:
				break
		except:
			print('Enter an integer between 3 and 10')
	return dimension

# Take the input of the letters used to determine the direction left, right, up, and down
# Return the four letters used respectively (tuple)
def take_direction_input():
	while True:
		try:
			direction = input('Enter four letters to move left, right, up and down: ')
			left, right, up, down = direction.split()
			break
		except:
			print('Enter four letters separated by space')
	return left, right, up, down

# To find the coordinate of the blank tile in the puzzle
# p_list: A list in the form of nested list [[row1], [row2], ..., [row(n)]]
# Return the coordinate as a list [row number, column number]
def blank(p_list):
	for x in range(len(p_list)):
		for y in range(len(p_list)):
			if p_list[x][y] == ' ':
				blank_space = [x, y]
	return blank_space

# To create a nested list of the randomized list and the ordered list
# p_dimension: The dimension of the puzzle (integer)
# Return two lists both in the form of nested list [[row1], [row2], ..., [row(n)]]
# blank(p_list) function should be called before this function
def table(p_dimension):
	number_list = list(range(1, p_dimension**2)) + [' ']
	answer_list = []

	while True:
		random_list = random.sample(number_list, len(number_list))
		table_list = []
		number_of_inversion = 0

		# To check the number of inversion (when the number inside a tile is larger than the tiles after it)
		for i in range(len(random_list)):
			for j in range (i+1, len(random_list)):
				if (random_list[i] != ' ') and (random_list[j] != ' '):
					if random_list[i] > random_list[j]:
						number_of_inversion += 1

		while random_list != []:
			table_list.append(random_list[:p_dimension])
			random_list = random_list[p_dimension:]

		blank_space = blank(table_list)
		blank_x = blank_space[0]
 
		# The criteria for the puzzle to be solvable
		if p_dimension%2 != 0 and number_of_inversion%2 == 0:
			break
		elif p_dimension%2 == 0:
			if (p_dimension-blank_x)%2 == 0 and number_of_inversion%2 != 0:
				break
			elif (p_dimension-blank_x)%2 != 0 and number_of_inversion%2 == 0:
				break

	while number_list != []:
		answer_list.append(number_list[:p_dimension])
		number_list = number_list[p_dimension:]
	
	return table_list, answer_list

# Print out the list in the form of a squared puzzle
# p_list: A list in the form of nested list [[row1], [row2], ..., [row(n)]]
def print_table(p_list):
	for x in range(len(p_list)):
		for y in range(len(p_list)):
			print('%4s'%p_list[x][y], end = '')
		print()
	return

# To check where the user can move to
# Return the direction prompted by the user (string)
def check_movement(
		p_blank_x,		# The row number of the blank tile in the puzzle (integer)
		p_blank_y, 		# The column number of the blank tile in the puzzle (integer)
		p_dimension, 	# The dimension of the puzzle (integer)
		p_left,			# The letter to move to the left (string)
		p_right,		# The letter to move to the right (string)
		p_up,			# The letter to move upward (string)
		p_down			# The letter to move downward (string)
		):
	valid_input = False
	while not valid_input:
		# If the blank tile is on the first row of the puzzle
		if p_blank_x == 0:
			# If the blank tile is on the top left corner of the puzzle
			if p_blank_y == 0:
				direction = input(f'Enter your move (left-{p_left} or up-{p_up}): ')
				if direction == p_left or direction == p_up:
					valid_input = True

			# If the blank tile is on the top right corner of the puzzle
			elif p_blank_y == p_dimension-1:
				direction = input(f'Enter your move (right-{p_right} or up-{p_up}): ')
				if direction == p_right or direction == p_up:
					valid_input = True
			
			else:
				direction = input(f'Enter your move (left-{p_left} or right-{p_right} or up-{p_up}:) ')
				if direction == p_left or direction == p_right or direction == p_up:
					valid_input = True
		
		# If the blank tile is on the last row of the puzzle
		elif p_blank_x == p_dimension-1:
			# If the blank tile is on the bottom left corner of the puzzle
			if p_blank_y == 0:
				direction = input(f'Enter your move (left-{p_left} or down-{p_down}): ')
				if direction == p_left or direction == p_down:
					valid_input = True

			# If the blank tile is on the bottom right corner of the puzzle
			elif p_blank_y == p_dimension-1:
				direction = input(f'Enter your move (right-{p_right} or down-{p_down}): ')
				if direction == p_right or direction == p_down:
					valid_input = True

			else:
				direction = input(f'Enter your move (left-{p_left} or right-{p_right} or down-{p_down}): ')
				if direction == p_left or direction == p_right or direction == p_down:
					valid_input = True
		
		# If the blank tile is on the first column of the puzzle
		elif p_blank_y == 0:
			direction = input(f'Enter your move (left-{p_left} or up-{p_up} or down-{p_down}): ')
			if direction == p_left or direction == p_up or direction == p_down:
					valid_input = True

		# If the blank tile is on the last column of the puzzle
		elif p_blank_y == p_dimension-1:
			direction = input(f'Enter your move (right-{p_right} or up-{p_up} or down-{p_down}): ')
			if direction == p_right or direction == p_up or direction == p_down:
					valid_input = True

		# If the blank tile is not on the borders of the puzzle
		else:											
			direction = input(f'Enter your move (left-{p_left} or right-{p_right} or up-{p_up} or down-{p_down}): ')
			if direction == p_left or direction == p_right or direction == p_up or direction == p_down:
					valid_input = True

	return direction

# To move the empty tile to the right
# Return the new list in the form of nested list [[row1], [row2], ..., [row(n)]]
def swap_left(
		p_list, 		# List in the form of nested list [[row1], [row2], ..., [row(n)]]
		p_dimension, 	# The dimension of the puzzle
		p_blank_x, 		# The row number of the blank tile in the puzzle
		p_blank_y		# The column number of the blank tile in the puzzle
		):
	p_list[p_blank_x][p_blank_y], p_list[p_blank_x][p_blank_y+1] = p_list[p_blank_x][p_blank_y+1], p_list[p_blank_x][p_blank_y]
	return p_list

# To move the empty tile to the left
# Return the new list in the form of nested list [[row1], [row2], ..., [row(n)]]
def swap_right(
		p_list,			# List in the form of nested list [[row1], [row2], ..., [row(n)]] 
		p_blank_x,		# The row number the blank tile in the puzzle 
		p_blank_y		# The column number of the blank tile in the puzzle
		):
	p_list[p_blank_x][p_blank_y], p_list[p_blank_x][p_blank_y-1] = p_list[p_blank_x][p_blank_y-1], p_list[p_blank_x][p_blank_y]
	return p_list

# To move the empty tile down
# Return the new list in the form of nested list [[row1], [row2], ..., [row(n)]]
def swap_up(
		p_list,			# List in the form of nested list [[row1], [row2], ..., [row(n)]] 
		p_dimension,	# The dimension of the puzzle 
		p_blank_x,		# The row number of the blank tile in the puzzle 
		p_blank_y		# The column number of the blank tile in the puzzle
		):
	p_list[p_blank_x][p_blank_y], p_list[p_blank_x+1][p_blank_y] = p_list[p_blank_x+1][p_blank_y], p_list[p_blank_x][p_blank_y]
	return p_list

# To move the empty tile up
# Return the new list in the form of nested list [[row1], [row2], ..., [row(n)]]
def swap_down(
		p_list,			# List in the form of nested list [[row1], [row2], ..., [row(n)]] 
		p_blank_x,		# The row number of the blank tile in the puzzle
		p_blank_y		# The column number of the blank tile in the puzzle
		):		
	p_list[p_blank_x][p_blank_y], p_list[p_blank_x-1][p_blank_y] = p_list[p_blank_x-1][p_blank_y], p_list[p_blank_x][p_blank_y]
	return p_list

# To play the game
def main():
	play = 'y'

	name = input('Enter your username: ')
	print('Welcome to the sliding puzzle game, ' + name + '!')
	print('Slide the adjacent tile until they are in a numerical order with the blank space at the right bottom corner of the puzzle')

	while play.lower() == 'y':
		count = 0
		dimension = take_dimension_input()
		lists = table(dimension)
		random_list = lists[0]
		answer_list = lists[1]
		left, right, up, down = take_direction_input()
		print_table(random_list)

		while random_list != answer_list:
			blank_space = blank(random_list)
			blank_x = blank_space[0]
			blank_y = blank_space[1]
			direction = check_movement(blank_x, blank_y, dimension, left, right, up, down)
			if direction == left:
				print_table(swap_left(random_list, dimension, blank_x, blank_y))
			elif direction == right:
				print_table(swap_right(random_list, blank_x, blank_y))
			elif direction == up:
				print_table(swap_up(random_list, dimension, blank_x, blank_y))
			elif direction == down:
				print_table(swap_down(random_list, blank_x, blank_y))
			count += 1

		if random_list == answer_list:
			print('Congratulations! You have finished the puzzle!')
			if count > 1:
				print('You used ' + str(count) + ' steps!')
			else:
				print('You used ' + str(count) + ' step!')
			play = input('Would you like to play again? \'y\' to play again: ')

	if play.lower() != 'y':
		print('Thank you for playing!')

	return

if __name__ == "__main__":
	main()