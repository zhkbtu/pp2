#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(x):
  for i in range(len(x)-1):
    if x[i:i+2] == [3,3]:
      return True
  return False
a= [int(x) for x in input().split()]
print(has_33(a))