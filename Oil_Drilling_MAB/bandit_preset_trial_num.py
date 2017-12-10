import slots
import random

num_spaces = int(input("How many grid spaces?"))
total_strategy_dict = ["eps_greedy", "softmax", "ucb", "bayesian"]
num_trials_arr = [100, 1000, 10000, 100000]


def main():
    ##randomly generates probability array
    probs_arr = []
    for i in range(0, num_spaces):
        prob = random.random()
        probs_arr.append(prob)
    for num in num_trials_arr:
        print("\nNumtrials: %s" %(num))
        ##for each strategy, decides which 3 spaces to drill in
        for strat in total_strategy_dict:
            tmp = list(probs_arr)
            b1 = run(tmp, strat, num)
            tmp[b1] = 0
            b2 = run(tmp, strat, num)
            tmp[b2] = 0
            b3 = run(tmp, strat, num)
            print("\n %s results:" %(strat))
            print("Drill in: %s -> %s -> %s" %(b1, b2, b3))
    ##outputs underlying probabilities
    print("\nTrue Probabilities: %s" %(probs_arr))
    count = 0
    _file = open("true_probs.csv", 'w')
    _file.close()
    _file = open("true_probs.csv", 'a')
    for prob in probs_arr:
        size = num_spaces**(.5)
        if (count < size):
            _file.write("%.2f," %(prob))
            count += 1
        elif(count == size):
            _file.write("\n%.3f," %(prob))
            count = 1
    _file.close

##creats a multi arm bandit and solves it given some probability list and a
##strategy
def run(probs_arr, strategy, num_trials):
    b = slots.MAB(probs = probs_arr)
    b.run(trials = num_trials, strategy=strategy)
    return  b.best()


if __name__ == '__main__':
  main()
