
def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    def count_helper(current_day: int, days: int) -> None:
        if current_day > days:
            print("Harvest time!")
            return
        else:
            print(f"Day {current_day}")
            count_helper(current_day + 1, days)
    count_helper(1, days)


if __name__ == "__main__":
    ft_count_harvest_recursive()
