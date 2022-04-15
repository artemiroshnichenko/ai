import matplotlib.pyplot as plt
import numpy as np
import math

class Approximate():

    def __init__(self, data=None, file=None) -> None:
        self.file = file
        if data == None and file!=None:
            self.read_file(file)
        elif self.data == None:
            raise Exception('Не задано данные')
        else:
            self.data = data
        self.x = np.arange(0, len(self.data), 1)
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.grid()
        if self.file != None:
            self.ax.set_title(f'Апроксимація даних {self.file}')
        else:
            self.ax.set_title('Апроксимація даних')

    def read_file(self, file: str) -> np.ndarray:
        self.data = np.loadtxt(file, delimiter='\t', dtype=np.float)
        return self.data

    def approximate(self, degree: int) -> np.ndarray:
        self.degree = degree   
        polinom = np.polyfit(self.x, self.data, degree)
        self.y = np.polyval(polinom, self.x)
        return self.y

    def add_data(self, style='o') -> None:
        self.ax.plot(self.x, self.data, style, label='Point')

    def add_approx(self, style='--g') -> None:
        self.ax.plot(self.x, self.y, style, label=f'Approx {self.degree}')
        self.ax.legend(loc='best')
        
    def save_plot(self, location: str) -> None:
        self.fig.savefig(location)

    def sd(self) -> float:
        sum = 0
        for i in range(len(self.data)):
            sum += (self.y[i] - self.data[i])**2
        sum = math.sqrt(sum/len(self.data))
        return sum


if __name__ == '__main__':
    pass
