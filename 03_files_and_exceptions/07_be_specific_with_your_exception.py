import os

try:
  file = open('sketch.txt')

  for line in file:
    try:
      (role, content) = line.split(': ', 1)
      print(role, ' said: ', content)
    except ValueError:
      pass

  file.close()
except IOError:
  print('The data file is missing')
