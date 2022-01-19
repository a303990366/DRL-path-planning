import numpy as np
import gym
from stable_baselines3.common.env_checker import check_env
from gym import spaces
import random
import matplotlib.pyplot as plt
from stable_baselines3 import DQN,PPO
import datetime
from stable_baselines3.common.monitor import Monitor
from env import MySim_D

if __name__=="__main__":
    
    # DQN,A2C,HER,PPO,QR-DQN,TRPO,Maskable PPO can use
    env=Monitor(MySim_D())
    model =DQN(policy="MlpPolicy", env=env,)
    model.learn(total_timesteps=4000)
    txt=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    model.save('test_{}'.format('1'))
##    plt.show()
##    plt.plot(env.get_episode_lengths())
##    plt.show()
##    plt.plot(env.get_episode_rewards())

    for i in range(10):
      obs = env.reset()
      start=obs
      for _ in range(1000):
          action, state = model.predict(observation=obs)
          #print(action,state)
          obs, reward, done, info = env.step(action)
          if done:
            break
      env.map.draw_path((env.path_xdata[0],env.path_ydata[1]),env.path_xdata,env.path_ydata)  
      plt.show()  
      #fg.figure.savefig('fig/test_{}.png'.format(i))
