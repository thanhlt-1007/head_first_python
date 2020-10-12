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

try:
  with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
    print(man, file = man_file)
    print(other, file = other_file)
except IOError as error:
  print('File error: ', str(error))
