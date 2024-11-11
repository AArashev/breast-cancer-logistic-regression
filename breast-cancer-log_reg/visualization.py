
import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_distributions(dataset):
    plt.figure(figsize=(20, 15))
    dataset.hist(bins=20, figsize=(20, 15))
    plt.suptitle('Feature Distributions', fontsize=16)
    plt.show()

def plot_correlation_heatmap(dataset):
    plt.figure(figsize=(10, 8))
    sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title('Feature Correlation Matrix')
    plt.show()

def plot_boxplots(dataset):
    plt.figure(figsize=(20, 15))
    for idx, column in enumerate(dataset.columns[:-1]):
        plt.subplot(4, 4, idx+1)
        sns.boxplot(data=dataset, x=column, color="orange")
        plt.title(f'Boxplot of {column}')
    plt.tight_layout()
    plt.show()
