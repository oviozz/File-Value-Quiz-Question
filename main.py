#import file - and seperates questions and answer to key,value (key = ques) (value = answer)

file = 'questions.txt'
d = {}
with open(file) as f:
    for line in f:
        (key, value) = line.strip().split(',')
        d[key] = value

# -----------------------------------------------------------
#checks if user answer is correct if so score+=1 else: score-=1
score = 0
while score != 10: # 10 round for user to answer
    for ques, answer in zip(d.keys(), d.values()):
        print(ques)
        x = input(': ')
        if x in answer:
            score += 1
        else:
            score -= 1
        print(score)
