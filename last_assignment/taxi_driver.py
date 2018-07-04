from collections import defaultdict
import numpy as np
import random
import dill as pickle  #?????
from time import sleep
import matplotlib.pyplot as plt
import gym, gym.spaces, os
import driver_constants

class taxi_driver:
    """Player of Open AI Gym Game, Taxi-v2"""

    def __init__(self,
                 env,
                 learning_rate=0.1,
                 discount_factor=0.99,
                 epsilon=1.0,
                 sleep=0,
                 initial_p=15,
                 try_count=100,
                 reduce_random_factor=True,
                 show_process=True,
                 show_score_and_count=False,
                 update_function=None):
        """Initialize parameters."""

        self.env = env
        self.brain = defaultdict(
            lambda: np.array([initial_p] * env.action_space.n))
        self.learning_rate = learning_rate
        self.discount_factor_for_future = discount_factor
        self.random_action_rate = epsilon
        self.state = env.reset()
        self.done = False
        self.accumulated_reward = 0
        self.total_step = 1
        self.sleep = sleep
        self.try_count = try_count
        self.accumulated_rewards = []
        self.show_process = show_process
        self.reduce_random_factor = reduce_random_factor
        self.show_score_and_count = show_score_and_count
        self.constants = driver_constants.driver_constants()
        if update_function == None:
            update_function = self.constants.Q
        self.update_function = update_function
        if show_process: env.render()

    def update_view(self):
        """update view by bringing back cursor."""
        print("\033[{}A".format(9))
        self.env.render()

    def show_score(self):
        """show accumulated score."""
        print("try_count: " + str(self.total_step))
        print("score: " + str(self.accumulated_reward))

    def dump(self):
        """dump object information."""
        print('driver_object\nlearning_rate:' + str(self.learning_rate) +
              '\ndiscount_factor_for_future:' +
              str(self.discount_factor_for_future) + '\nrandom_action_rate:' +
              str(self.random_action_rate) + '\naccumulated_reward:' + str(
                  self.accumulated_reward))

    def save_brain(self, file_name='brain.pickle'):
        """save driver's brain as a local file."""
        with open(file_name, mode='wb+') as f:
            pickle.dump(self.brain, f)

    def load_brain(self, file_name='brain.pickle'):
        """load driver's brain."""
        try:
            with open(file_name, mode='rb') as f:
                self.brain = pickle.load(f)
                return True
        except Exception:
            import traceback
            traceback.print_exc()  
            return False

    def trash_brain(self, file_name='brain.pickle'):
        """remove driver's brain from local directory."""
        try:
            os.remove(file_name)
            return True
        except Exception as ex:
            import traceback
            traceback.print_exc()
            return False

    def learn(self, optical=False):
        """learning process"""
        tmp_epsilon = self.random_action_rate
        for i in range(self.try_count):
            if self.update_function == self.constants.Q:
                self.q(optical)
            elif self.update_function == self.constants.Sarsa:
                self.sarsa(optical)
            else:
                assert (False)

            if self.show_score_and_count: self.show_score()
            self.accumulated_rewards.append(self.accumulated_reward)
            self.state = self.env.reset()
            self.done = False
            self.accumulated_reward = 0
            # 全然収束しない、かつ更新式ごとの違いが知りたいので、Epsilonを減らしていく。
            if self.reduce_random_factor:
                self.random_action_rate -= tmp_epsilon * 1.3 / self.try_count
                self.random_action_rate = max(self.random_action_rate, 0)
            self.total_step = 1
            if self.show_process: self.env.render()

    def sarsa(self, optical):
        """SARSA update function."""
        if random.random() > self.random_action_rate or optical == True:
            # choose optimal option.
            action = np.argmax(self.brain[self.state])
        else:
            action = self.env.action_space.sample()
        while not self.done:
            self.total_step += 1
            sleep(self.sleep)

            next_state, reward, self.done, info = self.env.step(action)

            if random.random() > self.random_action_rate or optical == True:
                # choose optical option.
                next_action = np.argmax(self.brain[self.state])
            else:
                next_action = self.env.action_space.sample()

#             # SARSA更新式
#             self.brain[self.state][
#                 action] = self.brain[self.state][action] + self.learning_rate * (
#                     reward + self.discount_factor_for_future * self.
#                     brain[next_state][next_action] -
#                     self.brain[self.state][action])
            
            # 効率が良い版
            self.brain[self.state][action] -= self.learning_rate * (
                self.brain[self.state][action] - reward -
                self.discount_factor_for_future * self.brain[next_state][next_action])

            self.state = next_state
            action = next_action

            self.accumulated_reward += reward
            if self.show_process: self.update_view()

    def q(self, optical):
        """Q update function."""
        while not self.done:
            self.total_step += 1
            sleep(self.sleep)

            if random.random() > self.random_action_rate or optical == True:
                # choose optimal option.
                action = np.argmax(self.brain[self.state])
            else:
                action = self.env.action_space.sample()

            pre_state = self.state
            self.state, reward, self.done, info = self.env.step(action)
            #             #Q 数式そのまま
            #             self.brain[pre_state][
            #                 action] = self.brain[pre_state][action] + self.learning_rate * (
            #                     reward + self.discount_factor_for_future * max(
            #                         self.brain[self.state]) -
            #                     self.brain[pre_state][action])

            # 効率が良い版
            self.brain[pre_state][action] -= self.learning_rate * (
                self.brain[pre_state][action] - reward -
                self.discount_factor_for_future * max(self.brain[self.state]))

            self.accumulated_reward += reward
            if self.show_process: self.update_view()

    def show_learning_curve(self):
        """plot the learning curve using accumulated_rewards."""
        plt.plot(self.accumulated_rewards)
        plt.savefig('learning_curve.png')
        plt.show()

    def act_optimally(self):
        """act optically without acting randomly."""
        self.learn(optical=True)
