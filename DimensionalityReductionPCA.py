import sklearn
from sklearn.decomposition import PCA


class PCA():
    def setup(self, n_components, dataframe, feat_cols):
        pca = PCA(n_components=3)
        pca_result = pca.fit_transform(dataframe[])




if __name__== "__main__":
    dimensionReduction = PCA()

