'''
@author: raghul

Once the program has identified the model file, it stores the initial model, observation
model and transition model as lists. For each observation sequence, we compute the probabilities.
Once all probabilities have been calculated, we find the most probable state sequence.
'''
from pprint import pprint

def chunks(l, n):
    # this function splits a list l into a list of lists of size n
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

model = raw_input("Enter model file: ")
test = raw_input("Enter test file: ")
arr = []
for line in open(model, "r"):
    arr.append(line)
#print arr
states = int(arr[0])
initial = map(float, arr[1].split()) # list containing initial probabilities 
transistion = chunks(map(float, arr[2].split()), states) # list of lists containing transistion probabilities
output = arr[4].split() # list containing possible outputs
observation = chunks(map(float, arr[5].split()), len(output)) # list of lists containing the observation probabilities
#print "states: ", states
#print "initial: ", initial
#print "transistion: ", transistion
#print "output: ", output
#print "observation: ", observation
sequence = [] # observation sequences read from the test file will be stored in this list
for line in open(test, "r"):
    sequence.append(line.split())
#print "sequence: ", sequence
for seq in sequence:
    state_sequence = []
    print "Observation sequence: ", seq
    seq_len = len(seq)
    prob = []
    for i in range(seq_len):
        index = output.index(seq[i])
        prob.append([])
        if (i == 0):
            for j in range(states):
                prob[-1].append([initial[j] * observation[j][index]])
            #index = prob.index(max(prob))
            #print "index: ", index
            #state_sequence.append(index)
        else:
            for j in range(states):
                sub_prob = []
                for k in range(states):
                    sub_prob.append(prob[-2][k][0] * transistion[j][k] * observation[j][index])
                prob[-1].append([max(sub_prob), sub_prob.index(max(sub_prob))])
    #pprint (prob)
    for i in xrange(seq_len-1, -1, -1):
        if (i == seq_len-1):
            state_sequence.insert(0, prob[i].index(max(prob[i], key=lambda x: x[0]))) # to prepend the probability to state_sequence
            next_up = max(prob[i], key=lambda x: x[0])[1]
        elif (i == 0):
            state_sequence.insert(0, next_up)
        else:
            state_sequence.insert(0, next_up)
            next_up = prob[i][next_up][1]
    for i in range(seq_len):
        if (state_sequence[i] == 0):
            state_sequence[i] = 's1'
        elif (state_sequence[i] ==   1):
            state_sequence[i] = 's2'
        else:
            state_sequence[i] = 's3'
    print "Most probable state sequence: ", state_sequence