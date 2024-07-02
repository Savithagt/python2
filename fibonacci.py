
def com_marks():
    num_students=int(input("Enter the number of Students:"))
    if num_students<=0:
        print("Enter the number greater than 0")
        return
    marks=[]
    for i in range(num_students):
        mark=float(input("Enter the marks of Students:"))
        marks.append(mark)

    highest_marks=max(marks)
    lowest_marks=min(marks)
    print("The highest mark is:",highest_marks)
    print("The lowest mark is:",lowest_marks)
com_marks()
    
