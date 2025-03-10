

testScore = 91.625
bonusAns = True

if testScore >= 90:
    if bonusAns:
        print('You passed the exam and received extra credit!')
    else:
        print('You passed the exam but did not receive extra credit!')
elif testScore == 0:
    print(' ')
else:
    print('You did not pass the exam.')



if bool(testScore):
    print('Thank you for taking this exam!')
elif not bool(testScore):
    print('It looks like you have not taken the exam!')
else:
    print('It looks like you have not taken the exam!')


if isinstance(testScore, int):
    print('All scores are rounded up to the nearest whole number.')
else:
    print('Please round your score up to the nearest whole number to determine your actual score.')
    



