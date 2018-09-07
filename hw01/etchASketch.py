#!/usr/bin/env python

print "Use 'w' to move up, 's' to move down, 'a' to move left, and 'd' to move right"
print "Press enter after each move. Enter 'q' to quit."

x = 0
y = 0

rows=input("Enter the number of rows: ")
cols=input("Enter the number of columns: ")
s = ['.']
for k in range(rows):
	s.append('.')

canvas = [s]

for m in range(cols):
	canvas.append([s])

#canvas[x][y]='x'
#for k in range(rows-1):
#	canvas[x][y]=canvas[x][y] + '.'

for i in range(len(canvas)):
	for j in range(len(canvas[i])):
		print(canvas[i][j])

while 1:
	move=raw_input("make a move")
	if move == 'd':
		if x < rows:
			x = x+1
	if move == 'a':
		if x != 0:
			x = x-1
	if move == 's':
		if y < cols:
			y = y+1
	if move == 'w':
		if y != 0:
			y = y-1
	if move == 'q':
		exit()

	canvas[x][y] = 'x'
	for i in range(len(canvas)):
        	for j in range(len(canvas[i])):
	                print(canvas[i][j])

