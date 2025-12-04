class Solution:
    def countCollisions(self, directions: str) -> int:
        # Feels so good that, I have recognized that this problem uses
        # stack pattern on my own. Ahh big moment!
        stack = []
        collitions = 0

        for movement in directions:
            while stack and stack[-1] == 'R':
                if movement == 'L':
                    collitions += 2
                    movement = 'S'
                    stack.pop()
                elif movement == 'S':
                    collitions += 1
                    stack.pop()
                else:
                    break

            while stack and stack[-1] == 'S':
                if movement == 'L':
                    collitions += 1
                    movement = 'S'
                    stack.pop()
                else:
                    break
            stack.append(movement)

        return collitions