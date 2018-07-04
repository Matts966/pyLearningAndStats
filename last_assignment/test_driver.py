import unittest
import taxi_driver
import gym, gym.spaces
import driver_constants

class TestDriver(unittest.TestCase):

    def test_epsilon(self):
        epsilon = 1.0
        reduce_param = 1.3
        try_count = 3
        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'), 
                try_count=try_count, reduce_random_factor=False, 
                epsilon=epsilon, show_process=False,
                show_score_and_count=False)
        self.assertEqual(t.random_action_rate, epsilon)
        t.learn()
        self.assertEqual(t.random_action_rate, epsilon)

        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'), try_count=3,
                show_process=False, show_score_and_count=False)
        self.assertEqual(t.random_action_rate, epsilon)
        t.learn()
        for i in range(3):
            epsilon -= reduce_param / try_count
            epsilon = max(epsilon, 0)
        self.assertEqual(t.random_action_rate, epsilon)
        
    def test_update_algorythm_type(self):
        constants = driver_constants.driver_constants()
        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'),
                show_process=False, show_score_and_count=False,
                update_function=constants.Q)
        self.assertEqual(t.update_function, constants.Q)

        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'),
                show_process=False, show_score_and_count=False,
                update_function=constants.Sarsa)
        self.assertEqual(t.update_function, constants.Sarsa)

    def test_reward_accumulation(self):
        try_count = 3
        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'),
                try_count=try_count, show_process=False,
                show_score_and_count=False)
        t.learn()
        self.assertEqual(try_count, len(t.accumulated_rewards))

    def test_brain_utils(self):
        t = taxi_driver.taxi_driver(env=gym.make('Taxi-v2'),
                show_process=False,
                show_score_and_count=False)
        self.assertFalse(t.load_brain(file_name='file_that_does_not_exist'))
        self.assertFalse(t.trash_brain(file_name='file_that_does_not_exist'))
        t.save_brain(file_name='temp.pickle')
        self.assertTrue(t.load_brain(file_name='temp.pickle'))
        self.assertTrue(t.trash_brain(file_name='temp.pickle'))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
