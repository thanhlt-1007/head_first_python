import pickle

def print_list_to_file(line_list, file):
  for line in line_list:
    print(line, file = file)

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
  with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
    pickle.dump(man, man_file)
    pickle.dump(other, other_file)
except IOError as error:
  print('File error: ', str(error))
except pickle.PickleError as error:
  print('Pickle error: ', str(error))

try:
  with open('man_data.txt', 'rb') as man_file, open('other_data.txt', 'rb') as other_file:
    pickle_man = pickle.load(man_file)
    pickle_other = pickle.load(other_file)

    print(man)
    print(other)
except IOError as error:
  print('File error: ', str(error))
except pickle.PickleError as error:
  print('Pickle error: ', str(error))
