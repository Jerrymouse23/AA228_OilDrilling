import slots
import random

num_spaces = int(input("How many grid spaces?"))
num_trials = int(input("How many trials?"))
total_strategy_dict = ["eps_greedy", "softmax", "ucb", "bayesian"]

def main():
    ##randomly generates probability array
    probs_arr = []
    for i in range(0, num_spaces):
        prob = random.random()
        probs_arr.append(prob)
    ##for each strategy, decides which 3 spaces to drill in
    for strat in total_strategy_dict:
        tmp = list(probs_arr)
        b1 = run(tmp, strat)
        tmp[b1] = 0
        b2 = run(tmp, strat)
        tmp[b2] = 0
        b3 = run(tmp, strat)
        print("\n %s results:" %(strat))
        print("Drill in: %s -> %s -> %s" %(b1, b2, b3))
    ##outputs underlying probabilities
    print("\nTrue Probabilities: %s" %(probs_arr))

##creats a multi arm bandit and solves it given some probability list and a
##strategy
def run(probs_arr, strategy):
    b = slots.MAB(probs = probs_arr)
    b.run(trials = num_trials, strategy=strategy)
    return  b.best()


if __name__ == '__main__':
  main()
