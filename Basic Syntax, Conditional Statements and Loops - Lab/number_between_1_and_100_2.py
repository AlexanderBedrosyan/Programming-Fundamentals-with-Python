def final_result():
    while True:
        command = float(input())
        if 1 <= command <= 100:
            print(f"The number {command} is between 1 and 100")
            break


final_result()