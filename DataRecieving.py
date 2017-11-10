import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''

We have to adrdress the specific way we will input data.
I will look it into more careful detail. It can be inputed with just
accelerometr values along with position values,
but the mapping itself may be different for just letters the 

'''


class DataRecieving():
    def __main__(self, filenames, complete_dataframes):
        self.read_Data(self, "testa.csv")
        complete_dataframes = self.read_Multiple_DataFiles(self,complete_dataframes,filenames)

        feature_names = complete_dataframes[0,0:len(complete_dataframes)]


    def read_Multiple_DataFiles(self, dataframes, filenames):
        for i in range(0,len(filenames)):
            dataframes[i] = pd.read_csv(filenames[i])
        return dataframes




if __name__ == "__main__":
    network = DataRecieving()
    dataframes = np.array(
    #create multiple arrays of zero values that will initialize later

    network.read_Multiple_DataFiles(self, )


