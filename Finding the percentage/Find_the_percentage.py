if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for name, line in student_marks.items():
        if query_name in name:
            for row in line:
                sum += row
            Average = float(sum/3)
    print ("%.2f" %(Average))
