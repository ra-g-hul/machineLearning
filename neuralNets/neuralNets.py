'''
@author: raghul
'''
import numpy as np

class neural_network:
    def __init__(self, features_len):        
        self.input_nodes = features_len
        self.output_nodes = 1
        #self.hidden_layer = 1
        #self.weight = np.random.randn(self.input_nodes, self.output_nodes)
        self.weight = np.zeros((self.input_nodes, self.output_nodes), dtype = float)
        
    def activation(self, z):
        return 1/(1+np.exp(-z))
    
    def activation_prime(self, z):
        return np.exp(-z)/((1+np.exp(-z))**2)
    
    def forward(self, x):
        self.z = np.dot(x, self.weight)
        self.y_hat = self.activation(self.z)
        return self.y_hat
        '''
        self.a_len = len(self.a)
        for i in range(self.a_len):
            if self.a[i] < 0.5:
                self.a[i] = 0
            else:
                self.a[i] = 1 
        return self.a
        '''
   
    def cost(self, x, y):
        self.y_hat = self.forward(x)
        J = 0.5*sum((y-self.y_hat)**2)
        return J
        
    def cost_prime(self, x, y):
        self.y_hat = self.forward(x)
        delta = np.multiply(-(y-self.y_hat), self.activation_prime(self.z))
        #print "delta: ", delta
        J_prime = np.dot(x.T, delta)
        return -J_prime #sign change

train = raw_input("Enter TRAINING file: ")
test = raw_input("Enter TESTING file: ")  
learning_rate = float(raw_input("Enter learning rate: "))
iterations = int(raw_input("Enter number of iterations: "))
#train = "train.dat.txt"
first = 0
features = []
attributes = [] # will contain attribute values and classes for each training instance 
for line in open(train, "r"):
    #print line
    a_line = line.split()
    if a_line != []:
        if first == 0:
            first += 1
            features = a_line
        else:
            a_line = map(int,a_line)
            attributes.append(a_line)
#print "features: ", features
#print "attributes: ", attributes
attributes_len = len(attributes)
x = [] # input
y = [] # output
for i in range(attributes_len):
    arr = attributes[i]
    y.append([arr.pop()])
    x.append(arr) 
x = np.array(x, dtype=float)
y = np.array(y, dtype=float)
#print "x: ", x
#print "y: ", y
# scaling, although not requires for binary values
x = x / np.amax(x, axis=0)
y = y / 1
#print "after scaling: "
#print "x: ", x
#print "y: ", y
#print "x.shape: ", x.shape
#print "y.shape: ", y.shape

NN = neural_network(len(features))
J = NN.cost(x,y)
J_prime = NN.cost_prime(x,y)
for i in range(iterations):
    NN.weight = NN.weight + (learning_rate*J_prime)
    J = NN.cost(x,y)
    J_prime = NN.cost_prime(x,y)
#print "cost: ", J

print "Classifing training instances..."
y_hat = NN.forward(x)
#print "y_hat :", y_hat
y_hat_length = len(y_hat)
for i in range(y_hat_length):
    if i >= 0.5:
        y_hat[i] = 1
    else:
        y_hat[i] = 0
#print "y_hat :", y_hat    
correct = 0   
for i in range(y_hat_length):
    if y[i] == y_hat[i]:
        correct += 1
accuracy = (float(correct)/y_hat_length) * 100
print "accuracy: ", accuracy

print "Classifing testing instances..."
test_attributes = []
first = 0
for line in open(test, "r"):
    a_line = line.split()
    if a_line != []:
        if first == 0:
            first += 1
        else:
            a_line = map(int,a_line)
            test_attributes.append(a_line)
attributes_len = len(test_attributes)
test_x = [] # input
test_y = [] # output
for i in range(attributes_len):
    arr = test_attributes[i]
    test_y.append([arr.pop()])
    test_x.append(arr) 
test_x = np.array(test_x, dtype=float)
test_y = np.array(test_y, dtype=float)
y_hat = NN.forward(test_x)
#print "y_hat :", y_hat
y_hat_length = len(y_hat)
for i in range(y_hat_length):
    if i >= 0.5:
        y_hat[i] = 1
    else:
        y_hat[i] = 0
#print "y_hat :", y_hat    
correct = 0   
for i in range(y_hat_length):
    if test_y[i] == y_hat[i]:
        correct += 1
accuracy = (float(correct)/y_hat_length) * 100
print "accuracy: ", accuracy
k=input("Press close to exit.") 
        
        
        
        
        
        
        
        


