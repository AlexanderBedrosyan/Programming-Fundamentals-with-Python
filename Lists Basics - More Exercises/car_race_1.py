timing = input()

timing_list = [int(ch) for ch in timing.strip().split()]
left_numbers = 0
right_numbers = 0

for i in range(len(timing_list) // 2):
    if timing_list[i] == 0:
        left_numbers *= 0.80
    if timing_list[-1 * abs(i + 1)] == 0:
        right_numbers *= 0.80

    left_numbers += timing_list[i]
    right_numbers += timing_list[-1 * abs(i + 1)]

if left_numbers < right_numbers:
    print(f"The winner is left with total time: {left_numbers:.1f}")
elif right_numbers < left_numbers:
    print(f"The winner is right with total time: {right_numbers:.1f}")
