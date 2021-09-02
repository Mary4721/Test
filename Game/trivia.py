score = 0
print('Hi, today we will play a trivia game')
print('RULES')
print('1. Please write all answers in lowercase.')
print('2. Each correct answer gives 5 points.')
print('3. Numbers are allowed.')
a= input('What is your name?:')
print('Welcome to the Quiz',a)
b= input('What is the capital of Columbia?\n')
if b=='bogota':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    print('Sorry.That is incorrect. The correct answer is bogota. You now have',score,'pointb.')
print('Next question')
c= input('What is the smallest planet?\n')
if c=='mercury':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    Score=0
    print('Sorry.That is incorrect. The correct answer is mercury. You now have',score,'pointc.')
d= input('How many deserts are in Africa?\n')
if d=='3':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    print('Sorry.That is incorrect. The correct answer is 3. You now have',score,'pointd.')
print('Next question')
e= input('What do you call a piece of land surrounding by water on 3 sides?\n')
if e=='peninsula':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    print('Sorry.That is incorrect. The correct answer is peninsula. You now have',score,'pointe.')
print('Next question')
f= input('Which is the tallest waterfall in the world?\n')
if f=='angel falls':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    print('Sorry.That is incorrect. The correct answer is angel falls. You now have',score,'pointf.')
print('Next question')
g= input('Where are the spanish steps located?\n')
if g=='rome':
    score = score+5
    print("That's right: You now have",score,'points.')
else:
    print('Sorry.That is incorrect. The correct answer is rome. You now have',score,'pointg.')
print('Congratulations you have reach the end, you can try later!')
 