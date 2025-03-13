# bounce.py
#
# Exercise 1.5

num_bounces = 0
height = 60

while num_bounces < 10:
  print(height)
  height /= 3/5 * height
