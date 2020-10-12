file = open('sketch.txt')

for line in file:
  if not line.find(':') == -1:
    (role, content) = line.split(': ', 1)
    print(role, ' said: ', content)

file.close()
