import tensorflow as tf 
import numpy as np  


class neuralNetwork:
    def __init__(self, input_data, label):
        self.input_data = input_data
        self.label = label
        self.X = tf.placeholder(tf.float32, (-1, self.input_data.shape[1]))
        self.Y = tf.placeholder(tf.float32, (-1, self.label.shape[1])

    def fc(self,
            self.input_data, 
            self.label, 
            hidden_layer_num,
            hidden_unit_num,
            ):
        theta = {}
        bias = {}
        if hidden_layer_num == 0:
            theta{str(0): tf.Variable(tf.random_normal((self.input_data.shape[1], self.label.shape[1])))}
            bias{str(0): tf.Variable(tf.random_normal((self.label.shape[1]))}
            return tf.multiply(X, theta['0']) + bias
        else:
             for i in range(hidden_layer):
                theta{str(i): tf.Variable(tf.random_normal(())) }
            

