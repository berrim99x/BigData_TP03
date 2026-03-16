import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(data):

    # Descriptive statistics
    print("\nDescriptive Statistics:")
    print(data.describe())

    # Correlation matrix
    print("\nCorrelation Matrix:")
    corr = data.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

    # Sales over time
    data.groupby('date')['sales'].sum().plot(kind='line')
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()