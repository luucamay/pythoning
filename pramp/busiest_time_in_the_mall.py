'''
Bussiest time in the mall

The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year.
You're given data extracted from the mall's door detectors.
Each data point is represented as an integer array whose size is 3.
The values at indices 0, 1 and 2 are the timestamp, the count of visitors,and whether 
the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively.
Here's an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch,
which is a nonnegative integer holding the number of seconds that
have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that
returns the time at which the mall reached its busiest moment last year.
The return value is the timestamp, e.g. 1480640292. 
Note that if there is more than one period with the same visitor peak,
return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp.
Explain your solution and analyze its time and space complexities.
'''
def find_busiest_period(data):  
  n = len(data)
  busiest_period = 0
  count_visitors = 0
  max_count_visitors = 0
  
  for i in range(0, n):
    # update count
    if data[i][2] == 0:
      count_visitors = count_visitors - data[i][1]
    else:
      count_visitors = count_visitors + data[i][1]
    # update maximum
    if i == (n - 1) or data[i][0] != data[i + 1][0]:
      new_total_visitors = count_visitors
      if new_total_visitors > max_count_visitors:
        busiest_period = data[i][0] # save timestamp
        max_count_visitors = new_total_visitors # update number of highest visitors
        
  return busiest_period

# Test cases
data = [[1487799425,14,1],
        [1487799425,4,1],
        [1487799425,2,1],
        [1487800378,10,1],
        [1487801478,18,1],
        [1487901013,1,1],
        [1487901211,7,1],
        [1487901211,7,1]]
# 1487901211
print find_busiest_period(data)