import matplotlib.pyplot as plt


#there are 3 types





def rndperm(args):
    rndperm = np.random.permutation(df.shape[0])


class t_SNE_Visualization():
    def Plot(self, points, labels, values):
        plt.gray()
        figure = plt.figure(figsize=(28,28))
        for i in range (0,30):
            ax = figure.add_subplot(3,10,i+1, title="Digit: " + str(df.loc[rndperm[i],'bold']))


    def Correlate(self, features, validation_set):

    def DimensionaltyReduction(self, correlated_variables):
        correlation_factors = correlated_variables[[i,0]:0]
        self.Correlate()

    def




if __name__ == "__main__":
    visualization = t_SNE_Visualization()


