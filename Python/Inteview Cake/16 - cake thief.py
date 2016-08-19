#16 - cake thief.py
import pdb

# weighs 7 kilograms and has a value of 160 pounds
(7, 160)

# weighs 3 kilograms and has a value of 90 pounds
(3, 90)

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20




def max_duffel_bag_value(cake_tuples, capacity):
#  pdb.set_trace()
  # rank by value/weight
  cake_tuples = sorted(cake_tuples, key = lambda x:x[1]/x[0], reverse = True)

  # Cake Index
  i = 0

  duffel_bag_value = 0
  # Fill the duffel bag
  while capacity > 0 and i <= len(cake_tuples)-1:
    cakes_added = int(capacity / cake_tuples[i][0])
    value_added = cakes_added * cake_tuples[i][1]
    capacity -= cakes_added * cake_tuples[i][0]
    duffel_bag_value += value_added
    #print 'Added %s cakes, totaling %s' % (cakes_added, value_added)

    # Move to next most valuable cake size
    i += 1
  print 'Stole %s GBP of cake! For the Queen!' % (duffel_bag_value)
  return(duffel_bag_value)

print(max_duffel_bag_value(cake_tuples, capacity))
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)

# Returns 0 if there is 0 capacity
print(max_duffel_bag_value(cake_tuples, 0))

print(max_duffel_bag_value([(5,5)], 4))
