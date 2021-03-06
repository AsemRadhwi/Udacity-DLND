from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        random.seed(0)
        self.synaptic_weights = 2 * random.random((3,1)) - 1

    def __sigmoid(self, x):
        return 1 / (1+exp(-x))

    #gradient descent
    def __sigmoid_derivative(self, x):
        return x * (1-x)

    def predict(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

    def train(self, training_set_inputs, training_set_outputs, number_of_iterations):
        print('training model')
        for iteration in range(number_of_iterations):

            #forward pass
            output = self.predict(training_set_inputs)

            #back pass
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

if __name__ == '__main__':

    #initialise a single neuron neural network
    nn = NeuralNetwork()

    print('Random starting synaptic weights:')
    print(nn.synaptic_weights)

    training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    nn.train(training_set_inputs, training_set_outputs, 10000)

    print('New synaptic weights after training:')
    print(nn.synaptic_weights)

    print('Considering new situation [1,0,0] -> ?:')
    print(nn.predict(array([1,0,0])) )