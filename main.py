from Engine.Loop import Pool
import pygame as py
py.init()
screen_size = (240, 135)
running = True

while running:
  running = Pool.loopy_doopy()
  loop_dict = Pool.loop_dict
  