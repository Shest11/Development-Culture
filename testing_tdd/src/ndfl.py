def calculate_ndfl_tax(income):
    # start, additional, rate
    tiers = [
        (0.0, 0.0, 0.13),
        (2_400_000.0, 312_000.0, 0.15),
        (5_000_000.0, 702_000.0, 0.18)
    ]
    for start, addition, rate in tiers:
        if income > start:
            return addition + (income-start) * rate
        return

    if income < 2_400_000:
        return income * 0.13
    elif income < 5_000_000:
        return (
            2_400_000 * 0.13 +
            (income - 2_400_000) * 0.15
        )
    elif income < 20_000_000:
        return (
            2_400_000 * 0.13 +
            2_600_000 * 0.15 +
            (income - 5_000_000) * 0.18
        )