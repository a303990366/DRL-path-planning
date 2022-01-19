# DRL-path-planning
Deep reinforcement learning


## 1.Introduction
#### We try to using deep reinforcement learning to make path planning in discrete observation space.
#### In this report,we test two algorithms:DQN and PPO.

## 2.requirement
--pip requirement.txt
## 3.enivroment setting
#### action space=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)] (eight actions)
#### observation space= 50*50 (means the enviroment contains 2500 spaces)
#### total_timesteps:40000000

## 4.reward
#### If agent arrive the goal,the agent get 500 rewards.
#### If agent touch the obstacle,the agent get -1000 rewards.
#### Agent will get rewards by distance between the agent location and the goal(Using Euclidean distance) at every step.

## 5.consequence



