import taxi_driver
import gym, gym.spaces

t = taxi_driver.taxi_driver(env = gym.make('Taxi-v2'), show_process=True, show_score_and_count=True, sleep=0.5)
t.learn()
