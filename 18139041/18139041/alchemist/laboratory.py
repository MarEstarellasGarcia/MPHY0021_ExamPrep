import random


class Laboratory(object):

    def __init__(self, shelf1, shelf2):
        self.shelf1 = shelf1
        self.shelf2 = shelf2

    def can_react(self, substance1, substance2):
        condition1 = (substance1 == "anti" + substance2)
        condition2 = (substance2 == "anti" + substance1)
        return condition1 or condition2

    def update_shelves(self, shelf1, shelf2, substance1, substance2_index):
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1+1:]
        shelf2 = self.shelf2[:substance2_index] + shelf2[substance2_index+1:]
        return shelf1, shelf2

    def do_a_reaction(self, shelf1, shelf2):
        for substance1 in shelf1:
            possible_targets = [i for i, target in enumerate(shelf2) if
                                self.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(shelf1, shelf2, substance1,
                                           substance2_index)
        return shelf1, shelf2

    def run_full_experiment(self, shelf1, shelf2):
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        return shelf1, shelf2, count
