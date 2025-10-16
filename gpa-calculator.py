def routine(credit,subject):
    gpa=0.00
    

    if credit==3:
        first_incourse_marks=float(input('your first incourse marks:'))
        second_incourse_marks=float(input('your second incourse marks:'))
        attendance=float(input('your attendance marks:'))
        avg_incourse=(first_incourse_marks+second_incourse_marks)/2
        ur_score=float(input("your expected marks in exam:"))
        score=ur_score+avg_incourse+attendance
        if subject=="lab":
            assesment=float(input("your assesment marks:"))
            score=score+assesment
    elif credit==2:
            incourse=float(input('your  incourse marks:'))
            attendance=float(input('your attendance marks:'))
            ur_score=float(input("your expected marks in exam:"))
            score=((ur_score+incourse+attendance)*100)/50
    if  score>=80 and score<=100:
            gpa=4.00
    elif  score>=75 and score<80:
        gpa=3.75
    elif  score>=70 and score<75:
        gpa=3.50
    elif  score>=65 and score<70:
        gpa=3.25
    elif  score>=60 and score<65:
        gpa=3.00
    elif  score>=55 and score<60:
        gpa=2.75
    elif  score>=50 and score<55:
        gpa=2.50
    elif  score>=45 and score<50:
        gpa=2.25
    elif  score>=40 and score<45:
        gpa=2.00
    else:
        gpa=0.00
    return gpa
s=0
total_credit=0
total_course=int(input("total number of course:"))
for i in range(1,total_course+1):
    course_credit=int(input("your course credit?:"))
    subject=input("course name:")
    if  course_credit==2 and subject=="viva" :
        gpa=float(input("your expected gpa:"))
        s=s+(gpa*course_credit)
        total_credit=total_credit+course_credit
    elif course_credit==3:
           
            my_gpa=routine(course_credit,subject)
            print(my_gpa)
            s=s+(my_gpa*course_credit)
            total_credit=total_credit+course_credit
    elif course_credit==2:
            
            my_gpa=routine(course_credit,subject)
            print(my_gpa)
            s=s+(my_gpa*course_credit)
            total_credit=total_credit+course_credit
    else:
        print("please give correct value")
        break
final_gpa=s/total_credit
print("your final gpa is",final_gpa)