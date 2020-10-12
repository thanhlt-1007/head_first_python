try:
  man = []
  other = []

  file = open('sketch.txt')

  for line in file:
    try:
      (role, content) = line.split(': ', 1)
      content = content.strip()
      if role == 'Man':
        man.append(content)
      elif role == 'Other Man':
        other.append(content)
    except ValueError:
      pass

  file.close()
except IOError:
  print('The data file is missing')

print(man)
print(other)
