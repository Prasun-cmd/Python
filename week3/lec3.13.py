#break keywords
email=input('enter the email')
for c in email:
    if(c=='@'):
        break#this break statement break the loop as it recaches certain condition
    print(c,end='')
print('')
for c in email:
    if(c=='@'):
        print('')
        continue #skip the steps
    print(c,end='')

    #pass is used to do nothing