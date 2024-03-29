import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class Canvas(FigureCanvas):
    def __init__(self, parent):

        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.setParent(parent)

    # TABU
    def plotting(self, values,filename='Tabu_Search'):
        self.ax.clear()
        self.ax.plot(values)
        self.ax.set(xlabel='Miesiąc', ylabel='Ilość pieniędzy',
                    title='Wykres wartości funkcji celu')
        self.ax.grid()
        self.draw()
        self.fig.tight_layout()
        self.fig.savefig('Wyniki/Wykresy/' + filename)

    # główny, liniowy plot
    def plot_main(self, gain, loss, filename):

        self.ax.clear()
        self.ax.plot(gain)
        self.ax.plot(loss)
        self.ax.set(xlabel='Nr miesiąca', ylabel='Ilość pieniędzy w zł',
                    title='Wykres zysku i strat')
        self.ax.grid()
        self.draw()
        self.fig.savefig('Wyniki/Wykresy/' + filename)

    # bar plot mniej szczegółowy
    def plot_bar(self, gain, loss, filename):
        self.ax.clear()
        self.ax.bar(1, sum(gain))
        self.ax.bar(2, sum(loss))
        self.ax.set(ylabel='Ilość pieniędzy w zł',
                    title='Porównanie zysków i strat')
        self.ax.set_xticks([1, 2], ['Zyski', 'Straty'])
        self.ax.grid(axis='y')
        self.draw()
        self.fig.savefig('Wyniki/Wykresy/' + filename)

    def plot_bar2(self, gain, loss, m, filename):
        self.ax.clear()
        labels = [f'm{i + 1}' for i in range(m)]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        self.ax.bar(x - width / 2, gain, width, label='Zyski')
        self.ax.bar(x + width / 2, loss, width, label='Straty')

        if m == 12:
            self.ax.set_xticks(x, labels)
        else:
            self.ax.set_xlabel('Numer miesiąca')
        self.ax.set_title(f'Wykres zysków i strat dla {m} miesięcy')
        self.ax.set_ylabel('Ilość pieniędzy w zł')
        self.ax.legend()
        self.ax.grid(axis='y')
        self.draw()
        self.fig.savefig('Wyniki/Wykresy/' + filename)



    # Ceny win

    def plot_vineprice(self, ch_types, num_of_years, bottle_prices,filename= 'ceny_wina.png'):
        self.ax.clear()
        self.fig.clf()

        colors = ['darkorchid','slateblue','darkgoldenrod',
                  'orangered','crimson','teal','steelblue','firebrick']

        c = 0
        if len(ch_types) > 4:
            k = 2
        else:
            k = 1
        months = num_of_years * 12

        for _, v in ch_types.items():
            if k >= 2:
                ax = self.fig.add_subplot(len(ch_types) - len(ch_types) // 2, k, c + 1)
            else:
                ax = self.fig.add_subplot(len(ch_types), k, c + 1)

            if num_of_years <= 2:
                ax.plot(range(1, months + 1), bottle_prices[c], linestyle='--', marker='o', c=colors[c])
            else:
                ax.plot(range(1, months + 1), bottle_prices[c], c=colors[c])
            ax.grid()
            ax.legend((v,), loc='best')

            c += 1

        self.fig.suptitle(f"Zmiana ceny wina na przestrzeni {months} miesięcy", y=0.97)
        self.fig.supylabel('Aktualna cena wina')

        if months == 12:
            month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            plt.xticks(range(1, months + 1), month)
            self.fig.supxlabel('Miesiąc')
        else:
            self.fig.supxlabel('Nr.miesiąca')
        self.fig.tight_layout()
        self.draw()
        self.fig.savefig('Wyniki/Wykresy/'+ filename)