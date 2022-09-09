'''''''''''''''''''''''''''''
N-Queens!
https://github.com/black-fractal/n-queens

@black-fractal
Vahid Khodabakhshi,
vkhodabakhshi@ce.sharif.edu
Initiated Date: January 2, 2021
Last modified date: January 9, 2021

'''''''''''''''''''''''''''''

import itertools
from time import sleep

COUNTER = 0

'''-----------------------------------------------------------------
The function checks that no two queens threaten each other.
thus, a solution requires that no two queens share the same
row, column, or diagonal. the function gets a list (each
element's index shows the row and element's value shows column
of located queen). In this formation no two queens are located
in the same row or column; So it is enough to check that no two
queens are in the same diagonal!
* returns True: IF no two queens threaten each other
* returns False: IF first two queens found that threaten each other
-----------------------------------------------------------------'''
def is_safe( o ):
    for i in range(len(o)):
        for j in range(len(o)):
            if i!=j:
                if abs(i-j)==abs(o[i]-o[j]):
                    return False
    return True

'''---------------------------------------------------------
The function makes a generator of safe formations and yield
each formation as a list of numbers. each element's index
shows the row and element's value shows column of located
queen. for example, [0, 3, 6, 9, 1, 8, 4, 2, 7, 5] represented
the following formation:
+-------------------------------+
| Q  .  .  .  .  .  .  .  .  .  |
| .  .  .  Q  .  .  .  .  .  .  |
| .  .  .  .  .  .  Q  .  .  .  |
| .  .  .  .  .  .  .  .  .  Q  |
| .  Q  .  .  .  .  .  .  .  .  |
| .  .  .  .  .  .  .  .  Q  .  |
| .  .  .  .  Q  .  .  .  .  .  |
| .  .  Q  .  .  .  .  .  .  .  |
| .  .  .  .  .  .  .  Q  .  .  |
| .  .  .  .  .  Q  .  .  .  .  |
+-------------------------------+
---------------------------------------------------------'''
def queens( n, second ):
    c = list( range(n) )
    for i in itertools.permutations( c ):
        if is_safe( i ):
            yield i
            sleep( second )

'''----------------------------------
The function print chess board
using ASCII characters as a table
----------------------------------'''
def ascii_chessboard_show( o, queen='Q', blank='.' ):
    global COUNTER
    COUNTER += 1
    l = len(o)
    # refresh output screen!
    # print(chr(27) + "[2J")
    print( '\n{}[{}]'.format( ' '*int(l*1.5), COUNTER ) )
    print( '+{}+'.format( '-'*(l*3+1) ) )
    for i in o:
        print( '| ', end='' )
        for j in range(l):
            if j==i:
                print( queen + '  ', end='' )
            else:
                print( blank + '  ', end='' )
        print( '|' )
    print( '+{}+'.format( '-'*(l*3+1) ) )

'''--------------
Main function.
--------------'''
def main():
    num_of_queens = 10
    sleep_seconds = 1
    for i in queens( num_of_queens, sleep_seconds ):
        print( i )
        ascii_chessboard_show( i, 'Q', '.' )

if __name__ == "__main__":
    main()