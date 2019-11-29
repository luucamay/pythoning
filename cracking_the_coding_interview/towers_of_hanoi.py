'''
Towers of Hanoi - Cracking the coding interview
Chapter 8, Problem #6
'''

def move_disks(n, source, destination, buffer):
    if n>0:
        move_disks(n-1, source, buffer, destination)
        move_top_to(source, destination)
        move_disks(n-1, buffer, destination, source)
def move_top_to(source, destination):
    disk = source.pop()
    destination.append(disk)
def towers_hanoi(n):
    tower1 = []
    tower2 = []
    tower3 = []
    for i in range(n, 0, -1):
        tower1.append(i)
    move_disks(n, tower1, tower3, tower2)
    print tower1, tower2, tower3

# Test
towers_hanoi(4)
