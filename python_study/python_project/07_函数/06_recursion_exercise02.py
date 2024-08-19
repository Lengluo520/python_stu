def peach(day):
    if day == 10:
        return 1
    else:
        return (peach(day + 1) + 1) * 2


print(peach(1))
