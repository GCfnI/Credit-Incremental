class Click:
  def __init__(self):
    self.clicked = False
  def click(self, klick):
    if klick:
      self.clicked = True
      return False
    elif self.clicked and not klick:
      self.clicked = False
      return True
    else:
      return False