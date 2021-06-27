import random as rand

max_val = 1_000_000
n = rand.randint(0, max_val)
user_input = -1
highest_low = 0
lowest_high = 1_000_000
guess_bar_length = 100
bar_per_max_val = max_val / guess_bar_length
left_range = 0
right_range = 0
middle_range = guess_bar_length

while user_input != n:
    print('░' * left_range + '▓' * middle_range + '░' * right_range)
    print('Lowest: ' + str(highest_low))
    print('Highest: ' + str(lowest_high))
    print('Enter your guess: ')
    user_input = int(input())
    if user_input > n:
        print('Lower!')
        lowest_high = min(lowest_high, user_input - 1)
        right_range = guess_bar_length - int(float(lowest_high / max_val) * guess_bar_length)
    elif user_input < n:
        print('Higher!')
        highest_low = max(highest_low, user_input + 1)
        left_range = int(float(highest_low / max_val) * guess_bar_length)

    middle_range = guess_bar_length - left_range - right_range

print('Great Job!')
