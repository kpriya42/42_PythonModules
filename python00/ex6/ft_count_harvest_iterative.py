
def ft_count_harvest_iterative() -> None:
    d = int(input("Days until harvest: "))
    days = range(1, d+1)
    for i in days:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
