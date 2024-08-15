while True:
    unites=(int(input('Enter number of unites  : ')))

    print(unites)
    if unites <= 100:
        print('bill = 0')
    elif unites <=200:
        bill = (unites - 100) * 5
        print(f'Your bill is {bill} RS')
    else:
        bill=(100 * 5)+(unites-200)* 10
        print(f'Your bill is {bill} RS')
