




def solution(A, B, C, D):
    hours = ""
    minutes = ""
    l = [A,B,C,D]
    firstHour = [2,1,0]
    for hour in firstHour:
        if hour in l:
            hours = hours+str(hour)
            l.remove(hour)
            break
    l = sorted(l,reverse=True)
    for hour in l:
        temp = hours+str(hour)
        if int(temp) < 24:
            hours = temp
            l.remove(hour)
            break
    if (len(hours)) < 2:
        return "NOT POSSIBLE"
    minutes1 = str(l[0])+str(l[1])
    minutes2 = str(l[1])+str(l[0])
    if int(minutes1) > 59 and int(minutes2) > 59:
        return "NOT POSSIBLE"
    elif int(minutes1) < 60 and int(minutes2) < 60:
        minutes = str(max(int(minutes1),int(minutes2)))
    else:
        minutes = str(min(int(minutes1),int(minutes2)))
    if int(minutes) == 0:
        minutes = minutes+"0"

    return hours+":"+minutes
    
    




print solution(0,0,0,0)
