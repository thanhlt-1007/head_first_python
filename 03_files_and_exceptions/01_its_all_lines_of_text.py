file = open('sketch.txt')

data = file.readline()
print(data, end="")
data = file.readline()
print(data, end="")

file.seek(0)
for line in file:
  print(line, end="")

file.close()
