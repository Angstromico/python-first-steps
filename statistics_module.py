import statistics

def main(): 
    samples = [10, 20, 30, 40, 50]

    avrg = statistics.mean(samples) # I can't call the Python as a module that's named statistics
    med = statistics.median(samples)
    var = statistics.variance(samples)

    print(f"Mean: {avrg}, Median: {med}, Variance: {var}")


if __name__ == "__main__":
    main()
