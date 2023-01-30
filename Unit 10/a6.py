def print_horizontal_lines(size):
    print(" ---- " * (size) )
def print_vertical_lines(size):
    print(" |   " * (size + 1) )

board_size = input("What game board size do you want? ")
board_size = int(board_size)

for i in range(board_size):
    print_horizontal_lines(board_size)
    print_vertical_lines(board_size)

print_horizontal_lines(board_size)