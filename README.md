# DRL-path-planning
Deep reinforcement learning


## 1.Introduction
#### We try to using deep reinforcement learning to make path planning in discrete observation space.
#### In this report,we test two algorithms:DQN and PPO.

## 2.Requirement
 * stable_baselines3
 * gym
 * numpy
 * random
 * matplotlib
## 3.Environment setting
* Action space = [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)] (eight actions)
> <img src="https://github.com/a303990366/DRL-path-planning/blob/main/Path%20Planning/agent.png" width="20%">
* Observation space = 50*50 (means the enviroment contains 2500 spaces)
* Number of obstacles = 40
* Total_timesteps = 4000000

## 4.Reward function
* If agent arrive the goal,the agent get 500 rewards.
* If agent touch the obstacle,the agent get -1000 rewards.
* Agent will get rewards by distance between the agent location and the goal(Using Euclidean distance) at every step.

## 5.Consequence
#### DQN-100 consequences(using 4 hours to train)
![image](https://github.com/a303990366/DRL-path-planning/blob/main/Path%20Planning/discrete/consequence.gif)
#### PPO-100 consequences(using 5.5 hours to train)
![image](https://github.com/a303990366/DRL-path-planning/blob/main/Path%20Planning/discrete/consequence_PPO.gif)
#### Fail case
![image](https://github.com/a303990366/DRL-path-planning/blob/main/Path%20Planning/discrete/test_8.png)

## 6.conclusion
Using the same setting, and we found DQN get better performance than PPO,PPO often stop when reaching the obstacle(like as section 5's fail case).
Although DQN have the same condition,but I beilive if we give more training,the agent will adjust the condition.
From this experience,I think reinforcement learning is very interesting technique,we don't need give labeled data,just provide some reward functions.By the way,I very like the concept in RL:exploration and exploitation.
