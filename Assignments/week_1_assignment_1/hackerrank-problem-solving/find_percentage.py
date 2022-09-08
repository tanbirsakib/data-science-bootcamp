if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks= student_marks[query_name]
    total_marks = 0
    for mark in marks:
        total_marks+= mark
    avg = total_marks/len(marks)
    print("%0.2f" %avg)
    
# Harsh 25 26.5 28
# Anurag 26 28 30
# Hars