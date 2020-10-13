def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)

  (mins, seconds) = time_string.split(splitter)
  return(mins + '.' + seconds)

def get_coach_data(file_name):
  try:
    with open(file_name) as file:
      data = file.readline()
    return(data.strip().split(','))
  except IOError as io_err:
    print('File error: ' + str(io_err))
    return(None)

sarah = get_coach_data('sarah.txt')
sarah_name, sarah_dob = sarah.pop(0), sarah.pop(0)
sanitize_data = [sanitize(time_string) for time_string in sarah]
unique_data = set(sanitize_data)
fasted_data = sorted(unique_data)[0:3]
print(str(fasted_data))
