def loading_bar(number):
    percent_loading = number / 10

    if percent_loading == 10:
        print("100% Complete!")
        print("[" + "%" * int(percent_loading) + "]")
    elif percent_loading < 10:
        print(f"{number}% " + "[" + "%" * int(percent_loading) + "." * (10 - int(percent_loading)) + "]")
        print("Still loading...")


number = int(input())

loading_bar(number)
