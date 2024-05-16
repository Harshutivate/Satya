def temp():
    temp = [23,24,25.6,28.8]
    return temp
def calc_ave(values):
    total = sum(values)
    average = total / len(values)
    return average
def calc_max_min(values):
    maxi = max(values)
    mini = min(values)
    return maxi ,mini

def main():
    values = temp()
    average = calc_ave(values)
    maxmin = calc_max_min(values)
    print("List of num entered: ",values)
    print("average: ",average)
    print("max and min",maxmin)

if __name__ == "__main__":
    main()