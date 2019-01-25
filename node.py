import random

class Node:
    def __init__(self, state, power):
        self.state = state
        self.power = power

    def get_node_state(self):
        return self.state

    def get_node_power(self):
        return self.power

    def propagate(self):
        if self.state == "Transfer":
            transfer_percentage = random.random()
            return transfer_percentage
        elif self.state == "Receive":
            demand_percentage = random.random()
            return demand_percentage
        else:
            return "Unknown State"

