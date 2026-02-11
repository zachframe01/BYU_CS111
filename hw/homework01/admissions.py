def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	

#cleaning the data to convert to a float. 
def convert_row_type(clean_split):
        #new code
        count = 1
        while count <= 8:
            clean_split[count] = float(clean_split[count])
            count += 1


# used to calculate the score of the student
def calculate_score(sat,gpa,interest, school):
    # 30% SAT
    # 40% GPA
    # 10% demonstrated interest
    # 20% high school quality

    gpa2 = ((gpa*2) * 0.4)
    sat2 = ((sat / 160) * 0.3)
    interest2 = (interest * 0.1)
    school2 = (school * 0.2)

    return (gpa2 + sat2 + interest2 + school2)

# function to find out if the student is an outlier
def is_outlier(interest, gpa, sat):
    return (interest == 0) or ((gpa * 2) - (sat / 160)  > 2)


# function to flag true if student is scoring 6 or an outlier. else the student is flagged as false. 
def calculate_score_improved(score, is_outlier):
    if score >= 6 or is_outlier:
        return True
    else:
         return False

def grade_outlier(grade):
    sorted_grade = sorted(grade)
    if ((sorted_grade[1]) - (sorted_grade[0])) > 20:
        return True
    else:
        return False
    

def grade_improvement(grade): 
    if (grade[0] <= grade[1] and grade[1] <= grade[2] and grade[2] <= grade[3]):
        return True
    else:
        return False
    




    
         
     
    



def main():

    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    
    scores_file = open("student_scores.csv", "w")
    chosen_file = open("chosen_students.csv", "w")
    outliers = open("outliers.csv", "w")
    chosen_improved = open("chosen_improved.csv", "w")
    better_improved = open("better_improved.csv", "w")
    composite_chosen = open("composite_chosen.csv", "w")
    

    print("Processing " + filename + "...")

    input_file.readline()
    


    for row in input_file:


        clean_split = row.strip()


        clean_split = (clean_split.split(","))


        convert_row_type(clean_split)


        name = clean_split[0]


        clean_split.pop(0)
        check_row_types(clean_split)


        score = (calculate_score(clean_split[0], clean_split[1], clean_split[2] , clean_split[3]))

        grades = (clean_split[4:8])
        

        scores_file.write(f"{name},{score:.2f}\n")


        if score > 6:
            chosen_file.write(f"{name}\n")


        outlier_status = (is_outlier(clean_split[2], clean_split[1], clean_split[0]))
        if outlier_status == True:
            outliers.write(f"{name}\n")


        if calculate_score_improved(score, outlier_status) == True and score >= 5:
            chosen_improved.write(f"{name}\n")

 
        if calculate_score_improved(score, outlier_status) == True:
            better_improved.write(f"{name},{clean_split[0]},{clean_split[1]},{clean_split[2]},{clean_split[3]}\n")


        if (score >= 6) or (score >= 5 and (is_outlier(clean_split[2], clean_split[1], clean_split[0])== True or grade_outlier(grades) == True or grade_improvement(grades) == True)):
            composite_chosen.write(f"{name}\n")
        
            



        


    



    #closing the files which were opened. 
    input_file.close()
    scores_file.close()
    chosen_file.close()
    outliers.close()
    chosen_improved.close()
    better_improved.close()
    composite_chosen.close()


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
