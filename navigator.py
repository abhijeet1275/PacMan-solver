from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        
        stack = Stack()
        stack.push((start, [start], self.dist(start, end)))
        
        if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException
        if (not (0<=start[0]<len(self.navigator_maze))) or (not (0<=start[1]<len(self.navigator_maze[0]))):
            raise PathNotFoundException
        if (not (0<=end[0]<len(self.navigator_maze))) or (not (0<=end[1]<len(self.navigator_maze[0]))):
            raise PathNotFoundException
            
        if start == end:
            return [start]
            
        visited = set()

        while not stack.empty():
            loc, path, last_score = stack.pop()
            
            if loc == end:
                return path
                
            visited.add(loc)

            x, y = loc
            
            possible_moves = [self.up, self.down, self.left, self.right]
            
            for move in possible_moves:
                loc_next = move(loc)
            
                if loc_next != (-1, -1):
                    x_next, y_next = loc_next
                    if (0 <= x_next < len(self.navigator_maze) and 0 <= y_next < len(self.navigator_maze[0]) and self.navigator_maze[x_next][y_next] == 0 and loc_next not in visited):
                        visited.add(loc_next)
                        distance = self.dist(loc_next, end)
                        stack.push((loc_next, path + [loc_next], distance))
            stack.sort()
        raise PathNotFoundException

    def dist(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def correct(self, loc):
        x, y = loc
        return (
            0 <= x < len(self.navigator_maze) and
            0 <= y < len(self.navigator_maze[0]) and
            self.navigator_maze[x][y] != 1  
        )

    def up(self, start):
        x, y = start
        if self.correct((x, y - 1)):
            return (x, y - 1)
        return (-1, -1)

    def down(self, start):
        x, y = start
        if self.correct((x, y + 1)):
            return (x, y + 1)
        return (-1, -1)

    def left(self, start):
        x, y = start
        if self.correct((x - 1, y)):
            return (x - 1, y)
        return (-1, -1)

    def right(self, start):
        x, y = start
        if self.correct((x + 1, y)):
            return (x + 1, y)
        return (-1, -1)
