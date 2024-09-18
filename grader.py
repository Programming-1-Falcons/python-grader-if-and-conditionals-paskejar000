def getAnswer(request): # Function for getting a specified answer
    if isinstance(request,str):
        return input('Enter ' + request + ': ')

def turnToInt(n): # Turns n into an integer if possible
    try:
        n = int(n)
        return n
    except:
        print("Value not recognized as an integer")
        return 'Invalid'
    
def grade(): # the main function
    total_pointsStr = getAnswer('Total Points') # Total points of assignment
    total_points = turnToInt(total_pointsStr)
    if total_points != 'Invalid':
        point_scoreStr = getAnswer('Student Score (in points)') #Student's scored points
        point_score = turnToInt(point_scoreStr)
        if point_score != 'Invalid':
            score_percentage = (point_score/total_points) * 100
            if score_percentage > 89: #A
                letter_grade = 'A'
            elif score_percentage > 76: #B
                letter_grade = 'B'
            elif score_percentage > 61: #C
                letter_grade = 'C'
            elif score_percentage > 51: #D
                letter_grade = 'D'
            else: #F
                letter_grade = 'F'
            # print final score
            print('Student scored: '+point_scoreStr+'/'+total_pointsStr+' = '+str(score_percentage)+'% ('+letter_grade+')')
        else:
            grade() #try again if invalid
    else:
        grade() #try again if invalid
        
grade()