import slots
import random

num_spaces = int(input("How many grid spaces?"))
num_trials = int(input("How many trials?"))
num_iterations = int(input("How many iterations?"))
total_eps_best_diff = 0.0
total_strategy_dict = {"eps_greedy" : 0.0, "softmax" : 0.0, "ucb" : 0.0, "bayesian":0.0}

##runs a multiple iteration using different ways of solving the bandit problem
##outputs comparison of best value found
def main():
    for trial in range(0, num_iterations):
        probs_arr = []
        ##fills in random true probabilities
        for i in range(0, num_spaces):
            prob = random.random()
            probs_arr.append(prob)
        for strat in total_strategy_dict:
            run(probs_arr, strat)
    ##outputs the average difference between the true probability of the one chosen
    ##and its expected payout
    for strat in total_strategy_dict:
        avg = total_strategy_dict[strat] / num_iterations
        print("%s best diff: %s" %(strat, avg))


##runs over given array for a partivular strategy. calculates expected payouts
##and compares to underlying probability
def run(probs_arr, strategy):
    b = slots.MAB(probs = probs_arr)
    b.run(trials = num_trials, strategy=strategy)

    best = b.best()
    payouts = b.est_payouts()
    actual = b.bandits.probs
    diff = abs(payouts[best] - actual[best])
    total_strategy_dict[strategy] += diff


if __name__ == '__main__':
  main()
