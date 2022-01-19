import gym
import numpy as np
from gym import spaces
import random
import matplotlib.pyplot as plt
from stable_baselines3.common.env_checker import check_env
from util import *
class MySim_D(gym.Env):
    def __init__(self):
        self.shape=(50,50)
        self.action_space=spaces.Discrete(8)
        self.observation_space=spaces.Discrete(self.shape[0]*self.shape[1])
        self.actions=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
        self.goal=(48,49)
        self.pro=preprocessing(self.shape)
        self.robot_location=None
        self.map=Map_D(self.goal,self.shape,40)
        self.dies_times=0#times of death
        self.arrive_times=0#times of arriving
        self.over_times=0
        self.step_times=0#caculate the steps of agent
        self.max_step=200#max step
    def step(self, action):
        state=self.get_obs(action)
        self.path_xdata.append(self.pro.index2loc(state)[0])
        self.path_ydata.append(self.pro.index2loc(state)[1])
        self.step_times+=1
        reward=self.get_reward(state)
        done,typ=self.get_done(state)
        info = {}
        return state, reward, done, info
    def reset(self):
      while True:
        state = self.observation_space.sample()
        if self.pro.index2loc(state) not in self.map.obstacle_list:
          break
      self.step_times=0
      self.robot_location=state
      self.path_xdata=[self.pro.index2loc(state)[0]]
      self.path_ydata=[self.pro.index2loc(state)[1]]
      return self.robot_location
    def render(self, mode='human'):
        pass
    def seed(self, seed=None):
        pass


    def get_reward(self,state):
      loc_goal=self.goal
      loc_state=self.pro.index2loc(state)
      total_rewards=0
      
      if state==self.pro.loc2index(self.goal):
        total_rewards+=500
      elif self.pro.index2loc(state) in self.map.obstacle_list:
        total_rewards-=1000
      else:
        distance=(((loc_goal[0]-loc_state[0])**2)+((loc_goal[1]-loc_state[1])**2))**0.5#L2 loss
        total_rewards-=distance
      return total_rewards
    def get_done(self,state):
      if state==self.pro.loc2index(self.goal):
        self.arrive_times+=1
        print('cumulative times:{0},steps:{1}'.format(self.arrive_times,self.step_times))#add
        return True,0
      elif self.pro.index2loc(state) in self.map.obstacle_list:
        self.dies_times+=1
        print('Die times:{0},steps:{1}'.format(self.dies_times,self.step_times))
        return True,1
      elif self.step_times>self.max_step:
        self.over_times+=1
        print('over max step times:{}'.format(self.over_times))
        return True,2
      else:
        return False,3
    def get_obs(self,action):
      now=self.pro.index2loc(self.robot_location)
      x = now[0]+self.actions[action][0]
      y = now[1]+self.actions[action][1]
      x=np.clip(x,0,self.shape[0]-1)#Maybe need to adjust lowwer limit
      y=np.clip(y,0,self.shape[1]-1)#Maybe need to adjust lowwer limit
      new_state=(x,y)

      self.robot_location=self.pro.loc2index(new_state)

      return self.robot_location

env = MySim_D()
check_env(env)

if __name__=="__main__":
    env = MySim_D()
    print(env)
    check_env(env)
