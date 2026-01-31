def ft_count_harvest_recursive(days, current=1):
    if current > days:
        return
    print("Day", current)
    ft_count_harvest_recursive(days, current + 1)
