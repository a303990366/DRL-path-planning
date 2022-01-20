# DRL-path-planning
Deep reinforcement learning


## 1.Introduction
#### We try to using deep reinforcement learning to make path planning in discrete observation space.
#### In this report,we test three algorithms:DQN,PPO and A2C.

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

## 5.Result
#### DQN-100 consequences(using 116.87 mins to train)
![image](https://github.com/a303990366/DRL-path-planning/blob/main/GIF/DQN.gif)
#### PPO-100 consequences(using 144.19 mins to train)
![image](https://github.com/a303990366/DRL-path-planning/blob/main/GIF/PPO.gif)
#### A2C-100 consequences(using 155.45 mins to train)
![image](https://github.com/a303990366/DRL-path-planning/blob/main/GIF/A2C.gif)
#### Fail case
![image](https://github.com/a303990366/DRL-path-planning/blob/main/Path%20Planning/discrete/test_8.png)
#### Detail
| Algorithm | average_reward  | average_lengths | average_spent_time |Find path(%)| Touch obstacle(%) | Over max step(%) | 
|-----------| --------------- | --------------- | ------------------ | ---------- |------------------ | ---------------- |
| A2C | -971.989  | 23.639  | 15.849   | 11.2 | 79.9 | 8.9 |
| PPO | -730.936  | 24.331  | 14.547   | 51.5 | 48.5 | 0.0 |
| DQN | -216.226  | 34.427  | 17.658   | 98.4 | 1.6 | 0.0 |
* From the table,we make testing 1000 times for three models,we found DQN get highest average rewards,but it need more times and steps to find path.
* We found DQN have 98.4% can find path;PPO have 51.5%;A2C have 11.2%.
* We found DQN have 1.6% touch obstacles;PPO have 48.5%;A2C have 79.9%.
* We found DQN have 0% over max step;PPO have 0%;A2C have 8.9%.
## 6.conclusion
* Using the same setting, and we found DQN get the best performance than others, DQN is critic approach,PPO and A2C are actor-critic approaches.Before I was made this,I expect PPO and A2C is better than DQN,but the result shows that DQN is better in this scene. 
* Although DQN have the some fail,but I beilive if we give more training(we just training around 2 hours),the agent will improve the condition.
* From this experience,I think reinforcement learning is very interesting technique,we don't need give labeled data,just provide some reward functions.By the way,I very like the concept in RL:exploration and exploitation.
* In future,I will construct the scene for avoiding dynamic obstacles and training agent in this.
* In this proposal, I provide three trained models,if someone want to test this can use them.
