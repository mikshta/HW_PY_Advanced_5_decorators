
import time


def logger_address(address):
  def logger(function):
    def new_function(*args, **kwargs):
      info_list = []
      date_and_time = time.ctime()
      function_name = function.__name__
      arguments = (f'arguments: {args}, {kwargs}')
      result = function(*args, **kwargs)
      info_list.append(date_and_time)
      info_list.append(function_name)
      info_list.append(arguments)
      print("loggger done")
      with open(address, "a+") as f:
        f.write(f"{info_list}")
        f.write('\n'*2)
      return result
    return new_function
  return logger


@logger_address('/Users/andreymikshta/Desktop/Netology/HW/AdvancedPY/logs.txt')
def multiplyer(a, c = 4):
  print('muliplyer func executed')
  return a * c

@logger_address('/Users/andreymikshta/Desktop/Netology/HW/AdvancedPY/logs.txt')
def complicated_func(d, e, h):
  g = d + e
  i = g / h
  print(f'g is {g}, complicated func executed')
  return f' some num is {g}, other num is {i}'

if __name__ == '__main__':
  multiplyer(2, 5)
  
  complicated_func(7,3,1)

  
  

