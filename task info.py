import csv
def write_file(info_list):
    with open("Student_info.csv','a',newline=")as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Year of Study", "Department",  "Contact Number", "E-Mail ID"])

        writer.writerow(info_list)

    if _name_ == '__main__':
     def Input_info(num):
                   temp_count = 1
                   while(temp_count<=num):
                       student_info = input("\n\nEnter the information of student #{}in the order of Name,Age,Year of Study,Department,Phone number and Email id:"
                                            .format(temp_count))
                       stud_info_list = student_info.split(" ")

                       print("\nThe entered info of student #{}is-\nName:{}\nAge:{}\nYear of study:{}\nDepartment:{}\nPhone Num:{}\nE-mail:{}"
                             .format(temp_count,stud_info_list[0],stud_info_list[1],stud_info_list[2],stud_info_list[3],stud_info_list[4],stud_info_list[5]))

                       choise_check ==input("\nnls tthe information provided correct?(yes/no):")

                       if choise_check =="yes":
                           write_file(stud_info_list)
                           temp_count += 1
                       elif choise_check == "no":
                           print("\nPlease re-enter the correct values!")
                           x=int(input("\nHow many student info do you want to enter?:"))
                           Input_Info(x)
                           extra = input("\nDo you want to enter anymore students infos?(yes/no):")
                           if extra =="yes":
                               new=int(input("\nHow many student info do you want to enter?:"))
                               Input_Info(new)
                           else:
                               print("\nThanks for providing the Student information!!")
