print("Decision on should i go to the market or not.")

decision = input("Am i out of shampoo? : ")

if decision in ('yes', 'no'):
    if 'yes' in decision:
        answer = input("is it raining? : ")
        if answer in ('yes', 'no'):
            if 'no' in answer:
                print("Yes go to the market.")
            elif 'yes' in answer:
                print("You don't go to the market lah, you just wash your car.")

    if "no" in decision:
        answer2 = input("Do you run out of cigarettes? : ")
        if answer2 in ('yes', 'no'):
            if 'yes' in answer2:
                print("Yes then go to the market.")
            elif 'no' in answer2:
                print("You don't need to go to the market lah!")

else:
    print("Please only answer with yes or no lah! ")