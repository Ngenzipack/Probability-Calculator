import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self, **samples):
    self.contents= []
    for colour, value in samples.items():
      for m in range(value):
        self.contents.append(colour) 

  def draw(self, removed):
    withdraw_list = copy.copy(self.contents)
    withdrawn = []
    if removed <= len(withdraw_list):
      for i in range(removed):
        drawn = random.randint(1, len(self.contents))
        drawn -= 1       
        the_withdrawn = self.contents.pop(drawn)
        withdrawn.append(the_withdrawn)
      return withdrawn
    else:
      return withdraw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  withdrawn_balls = []
  N = 0
  M = 0
  for i in range(num_experiments):
    the_balls = copy.deepcopy(hat)
    withdrawn_balls = the_balls.draw(num_balls_drawn)
    found = True
    for key in expected_balls.keys():
      if withdrawn_balls.count(key) < expected_balls[key]:
        found = False
        break
    if found:
      M = M +1 
    N = N + 1

  return M / N