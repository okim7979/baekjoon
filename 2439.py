N = int(input())
for number in range(N):
    text = ""
    for star in range(1, number+2):
        text = str(text) + str("*")
    print(text.rjust(N))