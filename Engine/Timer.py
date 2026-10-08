class Chronostalker:
  def __init__(self, time_dict):
    self.time_dict = time_dict
    self.timering = 0
    self.amount = 0
    self.completion = True
    self.paused = False
  def set_timer(self, amount):
    self.amount = amount
    self.completion = False
  def timer(self):
    if not self.completion:
      if not self.paused:
        self.timering += self.time_dict['dt']
      if self.timering >= self.amount:
        self.amount = self.timering
        self.completion = True
    return self.completion
  def progress_check(self):
    if self.amount == 0:
      return 0
    else:
      return self.timering / self.amount
    
class Watcher:
  def __init__(self, objecting):
    self.object = objecting
    self.iterations = 0
  def monitoring(self, reobject):
    if reobject == self.object:
      self.iterations += 1
      return False
    else:
      return True
  def reset(self):
    self.iterations = 0
  def get_iterations(self):
    return self.iterations