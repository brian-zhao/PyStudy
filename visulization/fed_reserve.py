import csv

import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = []
    y = []
    with open("FRB_H41_08_to_22.csv", "r") as csvfile:
        # skip first six rows
        for i in range(6):
            next(csvfile)
        plots = csv.reader(csvfile, delimiter=",")

        for row in plots:
            x.append(row[0])
            y.append(int(row[97]))
            print(row[0])

    plt.bar(
        x,
        y,
        color="g",
        width=0.5,
        label="Mortgage-backed securities: Wednesday level",
    )
    plt.xlabel("Date")
    plt.ylabel("USD * 1000000")
    plt.title("From 2008 to 2022")
    plt.legend()
    plt.show()
