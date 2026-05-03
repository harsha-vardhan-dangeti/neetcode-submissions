class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and asteroid < 0:

                top = stack[-1]

                if top < abs(asteroid):
                    stack.pop()
                elif top == abs(asteroid):
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive == True:
                stack.append(asteroid)
            
        return stack