import numpy as np
import random
import matplotlib.pyplot as plt

class preprocessing:
  '''the function for transform location and index'''
  def __init__(self,shape):
    self.shape=shape
    self.axis_dict=self.make_dict()
  def make_dict(self):
    '''produce a dict for checking(index,location)'''
    axis_list=[]
    for x in range(self.shape[0]):
      for y in range(self.shape[1]):
        axis_list.append((x,y))
    axis_dict=dict()
    for idx,axis in enumerate(axis_list):
      axis_dict[idx]=axis
    return axis_dict

  def loc2index(self,loc):
    '''turn location to index'''
    return list(self.axis_dict.values()).index(loc)
  def index2loc(self,idx):
    '''turn index to location'''
    return self.axis_dict[idx]

ob=[(16, 10),(40, 33),(38, 3),(24, 12),(18, 43),(35, 40),(34, 1),(31, 3),(42, 22),(43, 6),(48, 21),(26, 40),(44, 40),
    (49, 6),(17, 13),(39, 35),(20, 24),(26, 40),(17, 11),(16, 21),(1, 39),(12, 0),(31, 19),(8, 31),(16, 26),
    (1, 40),(47, 25),(50, 23),(12, 17),(50, 50),(19, 20),(46, 20),(35, 15),(4, 40),(10, 39),(49, 45),(31, 15),(49, 23),(15, 24),(47, 20)]
class Map_D:
  '''discrete map function'''
  def __init__(self,goal,grid_shape,number_obstacle):
    self.goal=goal
    self.grid_shape=grid_shape
    self.obstacle_list=self.random_obstacle(number_obstacle)
    self.obstacle_list=ob
    #self.obstacle_list=[(i,47) for i in range(0,45)]+[(i,40) for i in range(20,51)]
    self.map=self.making()
  def random_obstacle(self,times):
    '''produce serveral random obstacles'''
    tmp_obstacle_list=[]
    for i in range(times):
      x=random.randint(0,self.grid_shape[0])#adjust value
      y=random.randint(0,self.grid_shape[1])#adjust value
      if x!=self.goal[0] or y!=self.goal[1]:
        tmp_obstacle_list.append((x,y))
    return tmp_obstacle_list
  def making(self,start=None):
    '''make map'''
    figure, axes = plt.subplots()
    axes.set_xlim(0,self.grid_shape[0])#limit
    axes.set_ylim(0,self.grid_shape[1])#limit
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.grid()
    if start!=None:
        axes.plot(start[0],start[1],'r+',markersize=12)#start dot with red +
        axes.text(start[0],start[1],'start')#start text   
    axes.plot(self.goal[0],self.goal[1],'b*',markersize=12)#goal dot with blue *
    axes.text(self.goal[0]-1,self.goal[1]-1,'goal')#goal text
    for (ox, oy) in self.obstacle_list:
        #size**0.5 才是半徑
        axes.plot(ox, oy, "ok")
    return axes
  def draw_path(self,start,x_data,y_data):
    '''draw final path'''
    axes=self.making(start=list(start))
    axes.plot(x_data,y_data,'g--')
    return axes 
