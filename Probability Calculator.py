import copy
import random

class Hat:
    def __init__(self, **result):
        self.contents = []
        for k, v in result.items():
            self.contents.extend([k] * v)
            self.copy = self.contents.copy()

    def draw(self, num_to_draw):
        hat_list = []

        if num_to_draw >= len(self.contents):
            self.contents.clear()
            hat_list = self.copy
        else:
            for _ in range(num_to_draw):
                temp = self.contents.index(random.choice(self.contents))
                hat_list.append(self.contents.pop(temp))
        return hat_list

#returns the probability of drawing out expected balls / {num_experiments}
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments

    for i in range(N):
        trial_hat = copy.deepcopy(hat)
        result = trial_hat.draw(num_balls_drawn)

        drawn = {}
        for i in result:
            if i in drawn:
                drawn[i] += 1
            else:
                drawn[i] = 1

        fav_events = True
        for ball, count in expected_balls.items():
            if drawn.get(ball, 0) < count:
                fav_events = False
                break
        if fav_events:
            M += 1
    return M/N

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
    expected_balls={"red":2,"green":1},
    num_balls_drawn=5,
    num_experiments=2000)

print(probability)