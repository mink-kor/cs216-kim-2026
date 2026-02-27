# --------------------------------
# Exercise 1 – Clean Phone Numbers
# --------------------------------

phones = [
    "(260) 555-1234",
    "260.555.9876",
    "260-555-0000",
    "260  555 4321",
    "  260)555  2468 ",
    "  (260) 555-9999",
    "2605551111",
    "260-55-1234",
    "CALL: 260-555-1212 ext 9",
    "N/A"
]

for phone in phones:
    
    # Step 1: keep only digits
    digits = ""
    for ch in phone:
        if ch.isdigit():
            digits += ch
    
    # Step 2: validate length (must be 10 digits, else pring Invalid)
    if len(digits) != 10:
        print("Invalid")
    #note: 2605551234#
          #0123456789#
        
    # Step 3: if valid format as 260-555-1234 and print
    else:
        formatted = digits[0:3] + "-" + digits[3:6] + "-" + digits[6:10]
        print(formatted)
    

# ------------------------------------------
# 1. Utiizing String Methods to Clean Data
# ------------------------------------------
names = [
    "  moSes   ",
    "DAVID shepherd",
    "  maRy   magDalene  ",
    "pEter  fIsherman",
    "paUL apostle   ",
    "  estHER queen",
    "joSePh  ",
    "   saMUel prophet",
    "rUTH  gleaner ",
    "  soLoMon   king"
]

for name in names:
    name = name.strip()
    cleaned = ""
    for ch in name:
        if ch== " " and len(cleaned) > 0 and cleaned[-1] == " ":
            continue
        cleaned += ch
    cleaned = cleaned.title()
    
    # *** to do - clean data here ***
    print(cleaned)
    
    
    
    # end loop

# ------------------------------------------

# ------------------------------------------
# 3. Validate Course Codes (Regex)
# ------------------------------------------

import re

courses = [
    "CS111",
    "MATH101",
    "BIO202",
    "cs111",
    "CS-111",
    "CS11",
    "COMPSCI101",
    "ENGR10A",
    "HIST300"
]

pattern = r"[A-Z]{2,4}[0-9]{3}" # *** write your regex pattern here ***

for course in courses:

    # *** use re.fullmatch() to validate ***
    if re.fullmatch(pattern, course):
        print(course + " Valid ")
    else:
        print(course + " Not Valid ")
