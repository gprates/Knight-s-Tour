# Python program to for Knight's tour problem using
# Warnsdorff's algorithm
import random

class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y

tamanho_matriz = 8

# Move pattern on basis of the change of
# x coordinates and y coordinates respectively
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

# function restricts the knight to remain within
# the 8x8 chessboard
def is_movimento_valido(x, y):
	return ((x >= 0 and y >= 0) and (x < tamanho_matriz and y < tamanho_matriz))

# Checks whether a square is valid and empty or not
def is_vazio(a, x, y):
	return (is_movimento_valido(x, y)) and (a[y * tamanho_matriz + x] < 0)

# Returns the number of empty squares adjacent to (x, y)
def get_angulo(a, x, y):
	count = 0
	for i in range(tamanho_matriz):
		if is_vazio(a, (x + cx[i]), (y + cy[i])):
			count += 1
	return count

# Picks next point using Warnsdorff's heuristic.
# Returns false if it is not possible to pick
# next point.
def proximo_movimento(a, cell):
	min_deg_idx = -1
	c = 0
	min_deg = (tamanho_matriz + 1)
	nx = 0
	ny = 0

	# Try all tamanho_matriz adjacent of (*x, *y) starting
	# from a random adjacent. Find the adjacent
	# with minimum degree.
	start = random.randint(0, 1000) % tamanho_matriz

	for count in range(0, tamanho_matriz):
		i = (start + count) % tamanho_matriz
		nx = cell.x + cx[i]
		ny = cell.y + cy[i]
		c = get_angulo(a, nx, ny)
		if ((is_vazio(a, nx, ny)) and c < min_deg):
			min_deg_idx = i
			min_deg = c

	# IF we could not find a next cell
	if (min_deg_idx == -1):
		return None

	# Store coordinates of next point
	nx = cell.x + cx[min_deg_idx]
	ny = cell.y + cy[min_deg_idx]

	# Mark next move
	a[ny * tamanho_matriz + nx] = a[(cell.y) * tamanho_matriz + (cell.x)] + 1

	# Update next point
	cell.x = nx
	cell.y = ny

	return cell

# displays the chessboard with all the legal knight's moves
def print_grid(a):
	for i in range(tamanho_matriz):
		for j in range(tamanho_matriz):
			print("%d\t" % a[j * tamanho_matriz + i], end="")
		print()

# checks its neighbouring squares
# If the knight ends on a square that is one knight's move from the beginning square,then tour is closed
def is_vizinho(x, y, xx, yy):
	for i in range(tamanho_matriz):
		if ((x + cx[i]) == xx) and ((y + cy[i]) == yy):
			return True
	return False

# Generates the legal moves using warnsdorff's heuristics. Returns false if not possible
def find_movimento_valido():
	# Filling up the chessboard matrix with -1's
	a = [-1] * tamanho_matriz * tamanho_matriz

	# initial position
	sx = random.randint(0, tamanho_matriz - 1)
	sy = random.randint(0, tamanho_matriz - 1)

	# Current points are same as initial points
	cell = Cell(sx, sy)

	a[cell.y * tamanho_matriz + cell.x] = 1 # Mark first move.

	# Keep picking next points using Warnsdorff's heuristic
	ret = None
	for i in range(tamanho_matriz * tamanho_matriz - 1):
		ret = proximo_movimento(a, cell)
		if ret == None:
			return False

	# Check if tour is closed (Can end at starting point)
	if not is_vizinho(ret.x, ret.y, sx, sy):
		return False
	print_grid(a)
	return True


if __name__ == '__main__':
	while not find_movimento_valido():
		pass
