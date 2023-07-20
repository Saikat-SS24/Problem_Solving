# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction 
# (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for i in asteroids:
      if i > 0:
        stack.append(i)
      else:  # i < 0
        # Destroy previous positive one(s).
        while stack and stack[-1] > 0 and stack[-1] < -i:
          stack.pop()
        if not stack or stack[-1] < 0:
          stack.append(i)
        elif stack[-1] == -i:
          stack.pop()  # Both explode.
        else:  # stack[-1] > current
          pass  # Destroy current, so do nothing.

    return stack
