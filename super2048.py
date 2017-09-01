#!/usr/bin/python
#super2048 kickstart
#return list with all row reduce(2 - 1024).. AMAZING 
def _reduce(r ,grid , ini , l):
    i = ini
    while i >= 0:
        if bin(r + grid[i]).count('1') == 1:
            r += grid[i]
            grid[i] = 0
            i -= 1
        else:
            break
    l.append(r)
	#I don't know what happend here! really I don't know why set these conditions
    if len(grid) == 0 or len(grid) == 1 or i == -1:
        return l
    else:
        return _reduce(grid[i],grid[0:i + 1],i - 1,l)

#transponse of one matrix 
def flip(grid):
    _newGrid = [[0]*len(grid) for n in range(len(grid))]
    i = 0
    while i < len(grid):
        l2 = []
        j = 0
        while j < len(grid):
            l2.append(grid[j][i])
            j += 1
        _newGrid[i] = l2[:]
        i += 1
    return _newGrid

#validate DIR and set parameters
def gridReduce(grid,N,DIR):
    if DIR == 'up' or DIR == 'down':
        grid = flip(grid[:])
    newGrid = []
    for i in range(N):
        l = []
        _grid = [n for n in grid[i] if n != 0]
        if DIR == 'up' or DIR == 'left':
            _grid.reverse()
        if len(_grid) != 0:
            _red = _reduce(_grid[len(_grid) - 1],_grid,len(_grid) - 2,l)
        else:
            _red = [0]
        new = [0]*(N - len(_red))
        if DIR == 'down':
            _red.reverse()
        if DIR == 'up' or DIR == 'left':
            _red = _red + new
        else:
            _red = new + _red
            
        newGrid.append(_red)
    if DIR == 'up' or DIR == 'down':
        newGrid = flip(newGrid[:])
        
    return newGrid

#main here happend all! fuck awesome
if __name__ == '__main__':
    T = int(input())
    
    for t in range(1 , T + 1):
        N , DIR = input().split()
        N = int(N)
        grid = [[int(n) for n in input().split()] for i in range(N)]
        print("Case #{}:".format(t))
        outGrid = gridReduce(grid,N,DIR)
        y = ''
        for i in range(N):
            for j in range(N):
                y += str(outGrid[i][j]) + ' '
            print(y)
            y = ''
        
