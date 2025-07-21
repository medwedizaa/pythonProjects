auction_dict = {}
print("Hello to the auction bid")
entering = True

while entering:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    auction_dict[name] = bid

    answer = input("The next bid? y or n ")
    if answer != "y":
        entering = False

    print("\n" * 100)

best_name = ""
best_bid = 0
for key in auction_dict:
    if auction_dict[key] > best_bid:
        best_bid = auction_dict[key]
        best_name = key
print(f"The biggest bid was mabe by {best_name} and it is {best_bid}")

