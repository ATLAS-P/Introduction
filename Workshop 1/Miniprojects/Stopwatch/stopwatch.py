import time

last = time.time()
paused = False
total = 0
lap = 1
lapTime = 0


def show_time():
    print("%.3f" % total)


def show_lap_time():
    print("Lap " + str(lap) + ": " + "%.3f" % lapTime)


while True:
    x = input()

    new = time.time()

    if not paused:
        total += new - last
        lapTime += new - last

    last = new

    if x == "t":
        show_time()
    elif x == "p":
        if paused:
            paused = False
        else:
            show_time()
            paused = True
    elif x == "l":
        show_lap_time()
        lapTime = 0
        lap += 1
    elif x == "s":
        show_time()
        break