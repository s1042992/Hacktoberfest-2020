def check(years):
    if (years % 4) == 0:
        if (years % 100) == 0:
            if (years % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

if __name__ == '__main__':
	year = int(input("please enter a year:"))
	if(check(year)):
		print("It is a Leap Year")
	else:
		print("It is Not a Leap Year")
     
