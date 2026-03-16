from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def customer_segmentation(data):

    # Use sales only for clustering
    X = data[['sales']]

    kmeans = KMeans(n_clusters=3, random_state=42)
    data['cluster'] = kmeans.fit_predict(X)

    plt.scatter(data['customer_id'], data['sales'], c=data['cluster'])
    plt.title("Customer Segmentation")
    plt.xlabel("Customer ID")
    plt.ylabel("Sales")
    plt.show()

    return data