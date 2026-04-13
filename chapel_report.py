# chapel_report.py
# CS216
# 04.13.2026
# Min Kim

student_names = {} 

file = open("student.csv", "r")
line = file.readline()  

line = file.readline()
while line != "":
    parts = line.split(",")
    
    
    s_id = parts[0].strip()
    s_name = parts[1].strip()
    
    student_names[s_id] = s_name 
    
    line = file.readline()
file.close()



attendance_counts = {} 

file = open("attendance.csv", "r")
line = file.readline()  

line = file.readline()
while line != "":
    parts = line.split(",")
    
    
    s_id = parts[1].strip()
    
    
    if s_id not in attendance_counts:
        attendance_counts[s_id] = 0
    
    attendance_counts[s_id] += 1
    
    line = file.readline()
file.close()



out_file = "report.csv"
file = open(out_file, "w")


file.write("student_id, student_name, total_attended\n")


for s_id in student_names:
    name = student_names[s_id]
    
    
    count = 0
    if s_id in attendance_counts:
        count = attendance_counts[s_id]
    
    
    file.write(f"{s_id}, {name}, {count}\n")
    print(f" {s_id}, {name}, {count}") 

file.close()