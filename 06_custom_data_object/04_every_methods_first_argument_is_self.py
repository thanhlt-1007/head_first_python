class Athlete:
  def __init__(self, name, dob=None, times=[]):
    self.name = name
    self.dob = dob
    self.times = times

  def top_3_times(self):
    times = self.times
    sanitize_times = [self.sanitize(time_string) for time_string in times]
    unique_times = set(sanitize_times)
    top_3_times = sorted(unique_times)[0:3]
    return(top_3_times)

  def sanitize(self, time_string):
    if '-' in time_string:
      splitter = '-'
    elif ':' in time_string:
      splitter = ':'
    else:
      return(time_string)

    (mins, seconds) = time_string.split(splitter)
    return(mins + '.' + seconds)

  def add_time(self, time_value):
    self.times.append(time_value)

  def add_times(self, list_of_times):
    self.times.extend(list_of_times)

def get_coach_data(file_name):
  try:
    with open(file_name) as file:
      file_data = file.readline().strip().split(',')
      return(Athlete(file_data.pop(0), file_data.pop(0), file_data))
    return(data.strip().split(','))
  except IOError as io_err:
    print('File error: ' + str(io_err))
    return(None)

sarah = get_coach_data('sarah.txt')
print(str(sarah.top_3_times()))

sarah.add_time('1.23')
print(str(sarah.top_3_times()))

sarah.add_times(['0.12', '1.00'])
print(str(sarah.top_3_times()))
