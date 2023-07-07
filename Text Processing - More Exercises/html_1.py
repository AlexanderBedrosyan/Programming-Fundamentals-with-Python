counter = 0
while True:
    command = input()
    if command == "end of comments":
        break

    counter += 1

    if counter == 1:
        print(f"<h1>\n{command}\n</h1>")
    elif counter == 2:
        print(f"<article>\n{command}\n</article>")
    else:
        print(f"<div>\n{command}\n</div>")