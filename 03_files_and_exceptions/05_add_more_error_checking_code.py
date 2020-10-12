import os

if os.path.exists('sketch.txt'):
  file = open('sketch.txt')

  for line in file:
    try:
      (role, content) = line.split(': ', 1)
      print(role, ' said: ', content)
    except:
      pass

  file.close()
else:
  print('The data file is missing')
