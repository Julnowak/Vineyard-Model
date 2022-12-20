import matplotlib.pyplot as plt
import numpy as np

def main_plot(gain, loss):
    plt.plot(gain)
    plt.plot(loss)
    plt.title("Wykres zysku i strat")
    plt.grid()
    plt.legend(["zysk", "strata"])
    plt.show()

# TODO - ogarnąć wykres
def main_bar_plot(gain, loss, m):
    labels = [f'm{i+1}' for i in range(m)]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, gain, width, label='Zyski')
    ax.bar(x + width / 2, loss, width, label='Straty')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Ilość pieniędzy w zł')
    ax.set_title(f'Wykres zysków i strat dla {m} miesięcy')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.grid(axis='y')
    fig.tight_layout()
    plt.show()


def plot_2_bar_gain_and_loss(gain, loss):
    plt.bar(1, sum(gain))
    plt.bar(2, sum(loss))
    plt.title("Porównanie zysków i strat")
    plt.grid(axis='y')
    plt.xticks([1, 2], ['Zyski', 'Straty'])
    plt.ylabel('Ilość pieniędzy w zł')
    plt.show()


def sol_present_yourself(gain, loss, sol, ch_types):
    m = len(gain)
    print(f"Zysk z {m} miesięcy: {round(sum(gain),2)}\n")
    #print(f'Lista zysków: {gain}')
    print(f"Koszt z {m} miesięcy: {round(sum(loss),2)}\n")
    #print(f'Lista strat: {loss}')
    print(f"Bilans zysków i strat z {m} miesięcy: {round(sum(gain) - sum(loss),2)}\n")

    months = sol.shape[0]
    fields = sol.shape[1]
    grape_types = sol.shape[2]

    for m in range(months):
        mi = 0
        for f in range(fields):
            for t in range(grape_types):
                if sol[m][f][t] != 0:
                    if mi == 0:
                        print(f'\nW {m+1} miesiącu: ')
                        mi += 1

                    print(f'    na polu {f+1} zasadzono {int(sol[m][f][t])} jednostek winogron typu {ch_types[t+1]}.')

    main_plot(gain, loss)

    main_bar_plot(gain, loss, len(gain))

    plot_2_bar_gain_and_loss(gain, loss)


