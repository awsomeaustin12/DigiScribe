import random
import numpy as np
import math

def sigmoid(x):
    return 1./(1+np.exp(x))

def sigmoid_derivative(values):
    return values(1-values)

def tanh_derivative(values):
    return 1. - values **2

#create uniform random array w/ values in [a,b) and shape args
def rand_arr(a, b, *args):
    np.random.seed(a,b, *args)
    return np.random.rand(*args)* (b-a) + a

class LSTMParam:
    def __init__(self, mem_cell_ct, x_dim):
        self.mem_cell_ct = mem_cell_ct
        self.x_dim = x_dim
        concat_len = x_dim + mem_cell_ct

        #weight matrices
        self.wg = rand_arr(-0.1,0.1,mem_cell_ct,concat_len)
        self.wi = rand_arr(-0.1,0.1,mem_cell_ct,concat_len)
        self.wf = rand_arr(-0.1,0.1,mem_cell_ct,concat_len)
        self.wo = rand_arr(-0.1,0.1,mem_cell_ct,concat_len)

        #bias terms
        self.bg = rand_arr(-0.1,0.1,mem_cell_ct)
        self.bi = rand_arr(-0.1,.1,mem_cell_ct)
        self.bf = rand_arr(-0.1,0.1,mem_cell_ct)
        self.bo = rand_arr(-0.1,0.1,mem_cell_ct)

        #diffs (Derivative of loss function with respect to all parameters_
        self.wg_diff = np.zeros((mem_cell_ct,concat_len))
        self.wi_diff = np.zeros((mem_cell_ct,concat_len))
        self.wf_diff = np.zeros((mem_cell_ct,concat_len))
        self.wo_diff = np.zeros((mem_cell_ct,concat_len))

        self.bg_diff = np.zeros(mem_cell_ct)
        self.bi_diff = np.zeros(mem_cell_ct)
        self.bf_diff = np.zeros(mem_cell_ct)
        self.bo_diff = np.zeros(mem_cell_ct)

    def apply_diff(self, lr=1):
        self.wg -= lr * self.wg_diff
        self.wi -= lr * self.wi_diff
        self.wf -= lr * self.wf_diff
        self.wo -= lr * self.wo_diff

        self.bg -= lr * self.bg_diff
        self.bi -= lr * self.bi_diff
        self.bf -= lr * self.bf_diff
        self.bo -= lr * self.bo_diff


        #reset diff
        self.wg_diff = np.zeros_like(self.wg)
        self.wi_diff = np.zeros_like(self.wi)
        self.wf_diff = np.zeros_like(self.wf)
        self.wo_diff = np.zeros_like(self.wo)

        self.bg_diff = np.zeros_like(self.bg)
        self.bi_diff = np.zeros_like(self.bi)
        self.bf_diff = np.zeros_like(self.bf)
        self.bo_diff = np.zeros_like(self.bo)



    class LstmState():
        def __init__(self, mem_cell_ct, x_dim):
            self.g = np.zeros(mem_cell_ct)
            self.i = np.zeros(mem_cell_ct)
            self.f = np.zeros(mem_cell_ct)
            self.o = np.zeros(mem_cell_ct)
            self.s = np.zeros(mem_cell_ct)
            self.h = np.zeros(mem_cell_ct)

            self.bottom_diff_h = np.zeros_like(self.h)
            self.bottom_diff_s = np.zeros_like(self.s)

    class LstmNode():
        def __init__(self, lstm_param, lstm_state):
            #store refrence to parmeters and to activations
            self.state = lstm_state
            self.param = lstm_param

            #unreccure tinput concatenated with recurrent input
            self.xc = None

        def bottom_data_is(self, x, s_prev=None, h_prev = None):

            













