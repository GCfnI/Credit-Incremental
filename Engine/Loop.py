import pygame as py
from time import time

class Pool:
  time_started = False
  loop_dict = {}
  @staticmethod
  def loopy_doopy():
    if Pool.time_started is not True:
      Pool.past = time()
      Pool.time_started = True
    Pool.now = time()
    Pool.loop_dict['dt'] = (Pool.now - Pool.past)
    Pool.past = Pool.now
    for event in py.event.get():
      if event.type == py.QUIT:
         return False
    Pool.loop_dict['left_click'] = py.mouse.get_pressed()[0]
    Pool.loop_dict['right_click'] = py.mouse.get_pressed()[2]
    Pool.loop_dict['pos'] = py.mouse.get_pos()
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for letter in alphabet:
      Pool.loop_dict[letter] = py.key.get_pressed()[getattr(py, f'K_{letter}')]
    return True
    