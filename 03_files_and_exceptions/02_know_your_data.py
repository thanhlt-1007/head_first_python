file = open('sketch.txt')

for line in file:
  (role, content) = line.split(': ', 1)
  print(role, ' said: ', content)

file.close()
