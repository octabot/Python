n = int(input("Enter a number: "))
l = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
def say_digit(n):
    if n == 0:
        return
    say_digit(n//10)
    print(l[n%10], end=" ")
say_digit(n)
