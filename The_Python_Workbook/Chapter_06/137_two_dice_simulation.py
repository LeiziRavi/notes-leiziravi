import random

NUM_RUNS = 1000
D_MAX = 6


def rolling_dice():
    dice_01 = random.randrange(1, D_MAX+1)
    dice_02 = random.randrange(1, D_MAX+1)

    total = dice_01 + dice_02
    return total


def main():
    # Empty dictionary for simulation responses
    dice_sim_results = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                        7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    # Responses for 2-dice roll by probability theory
    expected_results = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
                        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 4.50, 12: 2.78}

    # Get the response for 1000 2-dice rolls
    for i in range(NUM_RUNS):
        total = rolling_dice()
        dice_sim_results[total] = dice_sim_results[total] + 1

    # Printing responses
    print(f"Total    Simulated     Expected")
    print(f"           Percent      Percent")
    for key in range(2, 13):
        print("%5d % 11.2f %8.2f" %
              (key, dice_sim_results[key]/NUM_RUNS * 100, expected_results[key]))


if __name__ == "__main__":
    main()
