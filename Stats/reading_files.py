import matplotlib.pyplot as plt

x = list()
y = list()

with open("data") as f:
    for line in f.readlines():
        data = line.split(",")

        x.append(float(data[0]))
        y.append(float(data[1]))

print(x)
print(y)

plt.scatter(x, y)
plt.show()