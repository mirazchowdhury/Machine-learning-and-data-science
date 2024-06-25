total_marks = int(input())

if total_marks <= 100 and total_marks >= 90:
    print("A")
elif total_marks < 90 and total_marks >= 80:
    print("B")
elif total_marks < 80 and total_marks >= 70:
    print("C")
elif total_marks < 70 and total_marks >= 60:
    print("D")
elif total_marks < 60 and total_marks >= 50:
    print("E")
elif total_marks < 50 and total_marks >= 40:
    print("E-")
elif total_marks < 40 and total_marks >= 0:
    print("F or Fail")
else:
    print("Error marks")


