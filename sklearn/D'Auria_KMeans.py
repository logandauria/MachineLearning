"""
Data clustering using KMeans
10/25/2020
@author: Logan D'Auria
"""

from sklearn.cluster import KMeans
import pandas as pd

# tag to print cluster info after computing
PRINT_CLUSTERS = True


def main():
    # load shopping data from a given csv file into a dataframe object using pandas
    shopping_data = pd.read_csv("HW_PCA_SHOPPING_CART_v896.csv")
    # drop the id column from the dataframe as it is not needed in analysis
    shopping_data = shopping_data.drop(columns=["ID"])

    # Create a new KMeans object using sklearn.cluster and call fit() to evaluate the data with given amount of clusters
    kmeans = KMeans(n_clusters=6, random_state=0).fit(shopping_data)

    if PRINT_CLUSTERS:
        print(kmeans.cluster_centers_)


if __name__ == '__main__':
    main()
