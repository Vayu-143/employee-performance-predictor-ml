import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance_distribution(data):
    sns.countplot(x="Performance", data=data)
    plt.title("Performance Distribution")
    plt.savefig("outputs/performance_distribution.png")
    plt.show()

def plot_confusion_matrix(cm):
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.savefig("outputs/confusion_matrix.png")
    plt.show()