import matplotlib.pyplot as plt


def plot(result_array):
    x_array = [i for i in range(len(result_array))]

    plt.plot(x_array, result_array, "o")
    plt.show()
