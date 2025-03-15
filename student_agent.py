import numpy as np
import pickle
import random
import os

class TaxiAgent:
    def __init__(self, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma
        print(f"Agent setting: alpha:{self.alpha}, gamma:{self.gamma}")
        self.load_q_table()

    def load_q_table(self, filename="final.pkl"):
        """
        Load Q-table from a file if it exists.
        """
        if os.path.isfile(filename):
            try:
                with open(filename, "rb") as f:
                    self.q_table = pickle.load(f)
                print(f"Loaded Q-table with {len(self.q_table)} states")
            except:
                print("Failed to load Q-table, initializing new one")
                self.q_table = {}
        else:
            print("No Q-table found, initializing new one")
            self.q_table = {}

    def save_q_table(self, filename="q_table.pkl"):
        """
        Save Q-table to a file.
        """
        with open(filename, "wb") as f:
            pickle.dump(self.q_table, f)

    def choose_action(self, state, epsilon):
        
        if state not in self.q_table:
            self.q_table[state] = np.zeros(6)
        
        if random.random() < epsilon:
            return random.randint(0, 5)  
        else:
            return np.argmax(self.q_table[state]) 
    def process_state(self, state):
        taxi_row, taxi_col, r_row, r_col, g_row, g_col, y_row, y_col, b_row, b_col, \
        obstacle_north, obstacle_south, obstacle_east, obstacle_west, \
        passenger_look, destination_look = state

        process_state = (
            (taxi_row, taxi_col),
            obstacle_north,
            obstacle_south,
            obstacle_east,
            obstacle_west
        )

        return process_state

    def update_q_value(self, state, action, reward, next_state, done):

        state = self.process_state(state)
        next_state = self.process_state(next_state)
        if state not in self.q_table:
            self.q_table[state] = np.zeros(6)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(6)
        current_q = self.q_table[state][action]
        max_next_q = np.max(self.q_table[next_state]) if not done else 0
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state][action] = new_q

agent = TaxiAgent(alpha=0.1, gamma=0.9)
epsilon = 1.0
def get_action(obs):

    global agent
    process_obs = agent.process_state(obs)
    action = agent.choose_action(process_obs, epsilon)

    return action# # Remember to adjust your student ID in meta.xml
# import numpy as np
# import pickle
# import random
# import gym 
# import os

# class TaxiAgent:
#     def __init__(self, alpha, gamma):
#         self.alpha = alpha
#         self.gamma = gamma
#         self.q_table = {}
#         self.load_q_table()

#         self.last_taxi_position = None
#         self.has_passenger = False
#         self.drop_off = False
#         self.target_passenger_station = None
#         self.target_passenger = None
#         self.target_destination_station = None
#         self.visited_passenger_station = set()
#         self.visited_destination_station = set()

#     def load_q_table(self, filename="q_table.pkl"):
#         """
#         Load Q-table from a file if it exists.
#         """
#         if os.path.isfile(filename):
#             try:
#                 with open(filename, "rb") as f:
#                     self.q_table = pickle.load(f)
#                 print(f"Loaded Q-table with {len(self.q_table)} states")
#             except:
#                 print("Failed to load Q-table, initializing new one")
#                 self.q_table = {}
#         else:
#             print("No Q-table found, initializing new one")
#             self.q_table = {}

#     def save_q_table(self, filename="q_table.pkl"):
#         """
#         Save Q-table to a file.
#         """
#         with open(filename, "wb") as f:
#             pickle.dump(self.q_table, f)

    
#     def choose_action(self, state, epsilon):
        
#         if state not in self.q_table:
#             self.q_table[state] = np.zeros(6)
        
#         if random.random() < epsilon:
#             return random.randint(0, 5)  
#         else:
#             return np.argmax(self.q_table[state]) 

#     def update_q_value(self, state, action, reward, next_state, done):
#         """
#         Update Q-value for a state-action pair.
#         """
#         # _, generalized_state = self.process_state(state)
#         # _, generalized_next_state = self.process_state(next_state)
        
#         # # Initialize Q-values if not seen before
#         # if generalized_state not in self.q_table:
#         #     self.q_table[generalized_state] = np.zeros(6)
#         # if generalized_next_state not in self.q_table:
#         #     self.q_table[generalized_next_state] = np.zeros(6)
        
#         # # Q-learning update
#         # current_q = self.q_table[generalized_state][action]
#         # max_next_q = np.max(self.q_table[generalized_next_state]) if not done else 0
#         # new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
#         # self.q_table[generalized_state][action] = new_q

#         if state not in self.q_table:
#             self.q_table[state] = np.zeros(6)
#         if next_state not in self.q_table:
#             self.q_table[next_state] = np.zeros(6)
#         current_q = self.q_table[state][action]
#         max_next_q = np.max(self.q_table[next_state]) if not done else 0
#         new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
#         self.q_table[state][action] = new_q

# agent = TaxiAgent(alpha=0.1, gamma=0.9)
# epsilon = 1.0
# def get_action(obs):

#     global agent 
#     action = agent.choose_action(obs, epsilon)
#     # taxi_passenger_dis, processed_state = agent.process_state(obs)
#     # agent.update_internal_state(obs)
#     # action = agent.choose_action(processed_state, epsilon)
#     # if taxi_passenger_dis == 0 and agent.has_passenger is False and action == 4:
#     #     agent.has_passenger = True
#     # if taxi_passenger_dis == 0 and agent.has_passenger is True and action == 5:
#     #     agent.has_passenger = False
#     #     agent.drop_off = True
#     #     agent.target_passenger = agent.last_taxi_position
#     # if taxi_passenger_dis == 0 and agent.drop_off is True and agent.has_passenger is False and action == 4:
#     #     agent.has_passenger = True
#     #     agent.drop_off = False
#     #     agent.target_passenger = None
  
#     return   action # 設定 ε-greedy 參數


#     # You can submit this random agent to evaluate the performance of a purely random strategy.

#     # TODO: Train your own agent
#     # HINT: If you're using a Q-table, consider designing a custom key based on `obs` to store useful information.
#     # NOTE: Keep in mind that your Q-table may not cover all possible states in the testing environment.
#     #       To prevent crashes, implement a fallback strategy for missing keys. 
#     #       Otherwise, even if your agent performs well in training, it may fail during testing.
# Remember to adjust your student ID in meta.xml
