#if condition

#Lets us consider a movie Avenger, this is a 13+ movie
print('Enter your date of birth')
date_ofyear=int(input())
current_year=2024

age=current_year-date_ofyear

if(age<13):
    print('you are underage ,you are not eligible to watch this movie')
else:
    print("you can watch the Avenger movie,Enjoy!")        