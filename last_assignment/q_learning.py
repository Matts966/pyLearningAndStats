import taxi_driver
import gym, gym.spaces

t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'), try_count=15000, 
        show_process=True, show_score_and_count=True)
t.learn()
t.show_learning_curve()
t.save_brain()
