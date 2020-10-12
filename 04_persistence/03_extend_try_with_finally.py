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
  man_file = open('man_data.txt', 'w')
  other_file = open('other_data.txt', 'w')

  print(man, file = man_file)
  print(other, file = other_file)
except IOError as error:
  print('File error: ', str(error))
finally:
  man_file.close()
  other_file.close()
