############################################################
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',
                             passwd='**********',database='IGDTUW')
mycursor=mydb.cursor()
def menu():
    print('\n\n\n')
    print('M E N U')
    print('1 for STUDENT RECORDS')
    print('2 for COURSE RECORDS')
    print('3 for EXAM RECORDS')
    print('4 for REPORT CARD FOR STUDENTS')
    print('5 to QUIT')
    choice=int(input('enter your choice (1/2/3/4/5)'))
    return choice
###########################################################
def add_student_record():
    try:
        admno=int(input('enter admission no of student: '))
        name=input('enter name of the student: ')
        fname=input('enter father\'s name of the student: ')
        mname=input('enter mother\'s name of the student: ')
        mno=int(input('enter mobile number: '))
        address=input('enter the address of the student: ')
        cat=input('enter the category (general/SC/ST/OBC/other)')
        dat=(admno,name,fname,mname,mno,address,cat)
        mycursor.execute('insert into student_info values(%s,%s,%s,%s,%s,%s,%s)',dat)
        mydb.commit()
        print('record added')
    except:
        print('problem in adding student data')
#########################################################
def display_all_student_data():
    try:
        query='select * from student_info'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        for rec in myrecords:
            print(rec)
    except:
        print('problem in displaying student data')
########################################################
def display_info_table():
    try:
        query='select * from student_info'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        print('IGDTUW'.center(90))
        print('Student Data'.center(90))
        print()
        print(105*'-')
        print('%-5s %-15s %-15s %-15s %-15s %-15s %-15s '\
              %('admno','name','father_name','mother_name','mobile_no','address','category'))
        print(105*'-')
        for rec in myrecords:
            print('%-5s %-15s %-15s %-15s %-15s %-15s %-15s '%rec)
        print(105*'-')
    except:
        print('Something went wrong')

#########################################################
def display_part_student_data():
    try:
        adm=input('enter the admission no of the student whose record is to be displayed: ')
        query='select * from student_info where admno='+"'"+str(adm)+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        print(myrecord)
        c=mycursor.rowcount
        if c==-1:
            print('nothing to display')
    except:
        print('problem in displaying particular record')
#########################################################
def delete_particular_student_record():
    try:        
        adm=input('Enter admission no. of the student whose record is to be deleted...')
        query='delete from student_info where admno='+"'"+adm+"'"
        mycursor.execute(query)
        mydb.commit()
        c=mycursor.rowcount
        if c>0:
            print('Deletion done')
        else:
            print('admission no ',adm,' not found')
    except:
        print('Something went wrong')
#########################################################
#########################################################
def modify_student_info():
    try:
        adm=input('Enter admission no. of the student whose record is to be modified...')
        query='select * from student_info where admno='+"'"+adm+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        c=mycursor.rowcount
        if c==-1:
            print('Admno '+adm+' does not exist')
        else:
            name=myrecord[1]
            fname=myrecord[2]
            mname=myrecord[3]
            mob_no=myrecord[4]
            address=myrecord[5]
            category=myrecord[6]
            print('admno :',myrecord[0])
            print('name :',myrecord[1])
            print('father_name :',myrecord[2])
            print('mother_name :',myrecord[3])
            print('mobile_no :',myrecord[4])
            print('aaddress :',myrecord[5])
            print('category :',myrecord[6])
            print('----------------------')
            ch='Y'
            while True:
                print('which record to be modified?')
                print('1.Name')
                print('2.Father name')
                print('3.Mother name')
                print('4.Mobile no')
                print('5.Address')
                print('6.Category')
                c=int(input('enter the data to be modified: '))
                if c==1:
                    nname=input('enter the new name: ')
                    query='update student_info set name='+"'"+nname+"'"+'where admno='+"'"+adm+"'"
                if c==2:
                    fname=input('enter the father name: ')
                    query='update student_info set father_name='+"'"+fname+"'"+'where admno='+"'"+adm+"'"
                if c==3:
                    mname=input('enter the mother name: ')
                    query='update student_info set mother_name='+"'"+mname+"'"+'where admno='+"'"+adm+"'"
                if c==4:
                    mob=input('enter the new mobile no: ')
                    query='update student_info set mobile_no='+"'"+mob+"'"+'where admno='+"'"+adm+"'"
                if c==5:
                    adr=input('enter the new address: ')
                    query='update student_info set address='+"'"+adr+"'"+'where admno='+"'"+adm+"'"
                if c==6:
                    cat=input('enter the new category: ')
                    query='update student_info set category='+"'"+cat+"'"+'where admno='+"'"+adm+"'"
                mycursor.execute(query)
                mydb.commit()
                ch=input('want to modify anything else(y/n): ')
                if ch.upper()=='Y':
                    continue
                else:
                    break
                print('Record modified')
    except:
        print('Something went wrong')

#########################################################
#########################################################
def add_course_details():
    try:
        course=input('enter the name of the course: ')
        code=input('enter the code of the course: ')
        sub1=input('enter subject 1: ')
        sub2=input('enter subject 2: ')
        sub3=input('enter subject 3: ')
        sub4=input('enter subject 4: ')
        sub5=input('enter subject 5: ')
        sub6=input('enter subject 6: ')
        core=(course,sub1,sub2,sub3,sub4,sub5,sub6,code)
        mycursor.execute('insert into course_data values (%s,%s,%s,%s,%s,%s,%s,%s)',core)
        mydb.commit()
        print('record added')
    except:
        print('problem in adding course data')
#########################################################
def display_all_course_data():
    try:
        query='select * from course_data'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        for rec in myrecords:
            print(rec)
    except:
        print('problem in displaying course data')
########################################################
def display_course_table():
    try:
        query='select * from course_data'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        print('IGDTUW'.center(90))
        print('Course Record'.center(90))
        print()
        print(125*'-')
        print('%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s'\
              %('course','sub1','sub2','sub3','sub4','sub5','sub6','c_code'))
        print(125*'-')
        for rec in myrecords:
            print('%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s'%rec)
        print(125*'-')
    except:
        print('Something went wrong')

#########################################################
def display_part_course_data():
    try:
        cod=input('enter the name of the course whose record is to be displayed: ')
        query='select * from course_data where c_code='+"'"+cod+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        print(myrecord)
        c=mycursor.rowcount
        if c==-1:
            print('nothing to display')
    except:
        print('problem in displaying particular course record')
#########################################################
def delete_particular_course_record():
    try:        
        cod=input('Enter admission no. of the student whose record is to be deleted...')
        query='delete from course_data where c_code='+"'"+cod+"'"
        mycursor.execute(query)
        mydb.commit()
        c=mycursor.rowcount
        if c>0:
            print('Deletion done')
        else:
            print('admission no ',cod,' not found')
    except:
        print('Something went wrong')
##########################################################
def modify_course_data():
    try:
        cod=input('Enter code of course whose record is to be modified...')
        query='select * from course_data where c_code='+"'"+cod+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        c=mycursor.rowcount
        if c==-1:
            print('code '+cod+' does not exist')
        else:
            course=myrecord[0]
            sub1=myrecord[1]
            sub2=myrecord[2]
            sub3=myrecord[3]
            sub4=myrecord[4]
            sub5=myrecord[5]
            sub6=myrecord[6]
            code=myrecord[7]
            print('course :',myrecord[0])
            print('sub1 :',myrecord[1])
            print('sub2 :',myrecord[2])
            print('sub3 :',myrecord[3])
            print('sub4 :',myrecord[4])
            print('sub5 :',myrecord[5])
            print('sub6 :',myrecord[6])
            print('c_code :',myrecord[7])
            print('----------------------')
            ch='Y'
            while True:
                print('which record to be modified?')
                print('1.Course name')
                print('2.sub1')
                print('3.sub2')
                print('4.sub3')
                print('5.sub4')
                print('6.sub5')
                print('7.sub6')
                c=int(input('enter the data to be modified: '))
                if c==1:
                    cour=input('enter the new name: ')
                    query='update course_data set course='+"'"+cour+"'"+'where c_code='+"'"+cod+"'"
                if c==2:
                    s1=input('enter the 1st subject name: ')
                    query='update course_data set sub1='+"'"+s1+"'"+'where c_code='+"'"+cod+"'"
                if c==3:
                    s2=input('enter the 2nd subject name: ')
                    query='update course_data set sub2='+"'"+s2+"'"+'where c_code='+"'"+cod+"'"
                if c==4:
                    s3=input('enter the 3rd subject name: ')
                    query='update course_data set sub3='+"'"+s3+"'"+'where c_code='+"'"+cod+"'"
                if c==5:
                    s4=input('enter the 4th subject name: ')
                    query='update course_data set sub4='+"'"+s4+"'"+'where c_code='+"'"+cod+"'"
                if c==6:
                    s5=input('enter the 5th subject name: ')
                    query='update course_data set sub5='+"'"+s5+"'"+'where c_code='+"'"+cod+"'"
                if c==7:
                    s6=input('enter the 6th subject name: ')
                    query='update course_data set sub6='+"'"+s6+"'"+'where c_code='+"'"+cod+"'"
                mycursor.execute(query)
                mydb.commit()
                ch=input('want to modify anything else(y/n): ')
                if ch.upper()=='Y':
                    continue
                else:
                    break
                print('Record modified')
    except:
        print('Something went wrong')

##########################################################
def add_student_score():
    try:
        print('Enter students information')
        admno=int(input('enter admission no of student'))
        name=input('enter name of the student')
        course=input('enter course: ')
        phy=int(input('Enter marks in SUB1: '))
        chem=int(input('Enter marks in SUB2: '))
        maths=int(input('Enter marks in SUB3: '))
        cs=int(input('Enter marks in SUB4: '))
        coa=int(input('Enter marks in SUB5: '))
        pyt=int(input('Enter marks in SUB6: '))
        wd=int(input('Enter the number of working days...'))
        ad=int(input('Enter the number of days student attended the class...'))
        r=(ad/wd)*100
        atten=round(r,2)
        total=phy+chem+maths+cs+coa+pyt
        perc=total/6
        if perc>=90:
            grade='A'
        elif perc>=80:
            grade='B'
        elif perc>=70:
            grade='C'
        elif perc>=60:
            grade='D'
        elif perc>=50:
            grade='E'
        else:
            grade='F'
        rec=(admno,name,course,phy,chem,maths,cs,coa,pyt,total,perc,atten,grade)
        mycursor.execute('insert into student_record values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',rec)
        mydb.commit()
        print('Record added')
    except:
        print('problem in adding student scores')
##########################################################
def display_all_student_records():
    try:
        query='select * from student_record'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        for rec in myrecords:
            print(rec)
    except:
        print('problem in displaying student record')
#########################################################
def display_part_student_record():
    try:
        adm=input('enter the admission no of the student whose record is to be displayed: ')
        query='select * from student_record where adm_no='+"'"+adm+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        print(myrecord)
        c=mycursor.rowcount
        if c==-1:
            print('nothing to display')
    except:
        print('problem in displaying particular student score record')
#########################################################
def display_score_table():
    try:
        query='select * from student_record'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        print('IGDTUW'.center(90))
        print('Student Record'.center(90))
        print()
        print(135*'-')
        print('%-5s %-15s %-8s %-8s  %-8s  %-8s  %-8s  %-8s  %-8s  %-9s %-8s %12s %12s'\
              %('admno','name','course','sub1','sub2','sub3','sub4','sub5','sub6','total','perc','attendance','div'))
        print(135*'-')
        for rec in myrecords:
            print('%-5s %-15s %-8s %-8s  %-8s  %-8s  %-8s  %-8s  %-8s  %-9s %-8s %12s %12s'%rec)
        print(135*'-')
    except:
        print('Something went wrong')
#########################################################       
def delete_particular_score_record():
    try:        
        adm=input('Enter admission no. of the student whose record is to be deleted...')
        query='delete from student_record where adm_no='+adm
        mycursor.execute(query)
        mydb.commit()
        c=mycursor.rowcount
        if c>0:
            print('Deletion done')
        else:
            print('admission no ',adm,' not found')
    except:
        print('Something went wrong')

##########################################################
##########################################################
def modify_score_record():
    try:
        adm=input('Enter admission no. of the student whose record is to be modified...')
        query='select * from student_record where adm_no='+"'"+adm+"'"
        mycursor.execute(query)
        myrecord=mycursor.fetchone()
        c=mycursor.rowcount
        if c==-1:
            print('Admno '+adm+' does not exist')
        else:
            name=myrecord[1]
            course=myrecord[2]
            sub1=myrecord[3]
            sub2=myrecord[4]
            sub3=myrecord[5]
            sub4=myrecord[6]
            sub5=myrecord[7]
            sub6=myrecord[8]
            att=myrecord[11]
            print('admno :',myrecord[0])
            print('name :',myrecord[1])
            print('course :',myrecord[2])
            print('sub1 :',myrecord[3])
            print('sub2 :',myrecord[4])
            print('sub3 :',myrecord[5])
            print('sub4 :',myrecord[6])
            print('sub5 :',myrecord[7])
            print('sub6 :',myrecord[8])
            print('total :',myrecord[9])
            print('percentage :',myrecord[10])
            print('attendance :',myrecord[11])
            print('grade :',myrecord[12])
            print('----------------------')
            ch='Y'
            while True:
                print('which record to be modified?')
                print('1.Name')
                print('2.Course')
                print('3.Marks')
                print('4.Attendance')
                c=int(input('enter the data to be modified: '))
                if c==1:
                    nname=input('enter the new name: ')
                    query='update student_record set name='+"'"+nname+"'"+'where adm_no='+"'"+adm+"'"
                if c==2:
                    ncour=input('enter the new course:')
                    query='update student_record set course='+"'"+ncour+"'"+'where adm_no='+"'"+adm+"'"
                if c==3:
                    print('1.sub1')
                    print('2.sub2')
                    print('3.sub3')
                    print('4.sub4')
                    print('5.sub5')
                    print('6.sub6')
                    c1=int(input('enter the subject whose marks to be updated: '))
                    if c1==1:
                        sub1=int(input('enter new marks in sub1: '))
                        query='update student_record set sub1='+"'"+str(sub1)+"'"+'where adm_no='+"'"+adm+"'"
                    if c1==2:
                        sub2=int(input('enter new marks in sub2: '))
                        query='update student_record set sub2='+"'"+str(sub2)+"'"+'where adm_no='+"'"+adm+"'"
                    if c1==3:
                        sub3=int(input('enter new marks in sub3: '))
                        query='update student_record set sub3='+"'"+str(sub3)+"'"+'where adm_no='+"'"+adm+"'"
                    if c1==4:
                        sub4=int(input('enter new marks in sub4: '))
                        query='update student_record set sub4='+"'"+str(sub4)+"'"+'where adm_no='+"'"+adm+"'"
                    if c1==5:
                        sub5=int(input('enter new marks in sub5: '))
                        query='update student_record set sub5='+"'"+str(sub5)+"'"+'where adm_no='+"'"+adm+"'"
                    if c1==6:
                        sub6=int(input('enter new marks in sub6: '))
                        query='update student_record set sub6='+"'"+str(sub6)+"'"+'where adm_no='+"'"+adm+"'"
                if c==4:
                    a=int(input('enter total number of working days: '))
                    b=int(input('enter number of days student attended the classes: '))
                    att=(b/a)*100
                    query='update student_record set attendance='+"'"+str(att)+"'"+'where adm_no='+"'"+adm+"'"
                total=sub1+sub2+sub3+sub4+sub5+sub6
                perc=total/6
                if perc>=90:
                    grade='A'
                elif perc>=80:
                    grade='B'
                elif perc>=70:
                    grade='C'
                elif perc>=60:
                    grade='D'
                elif perc>=50:
                    grade='E'
                else:
                    grade='F'
                query1='update student_record set total='+"'"+str(total)+"'"+','+'percentage='+"'"+str(perc)+"'"+','+\
                       'grade='+"'"+str(grade)+"'"+'where adm_no='+adm
                mycursor.execute(query1)
                rec =(adm,name,course,sub1,sub2,sub3,sub4,sub5,sub6,total,perc,att,grade)
                mycursor.execute(query)
                mydb.commit()
                ch=input('want to modify anything else(y/n): ')
                if ch.upper()=='Y':
                    continue
                else:
                    break
                print('Record modified')
    except:
        print('Something went wrong')
#############################################################
#############################################################
def menu2():
    print('1 for CREATE')
    print('2 for DISPLAY ALL RECORDS')
    print('3 for DISPLAY A PARTICULAR RECORD')
    print('4 for UPDATE')
    print('5 for DELETION')
    ch1=int(input('enter the choice in student records (1/2/3/4): '))
    return ch1
#############################################################
def report_card_all():
    try:
        query='select * from student_record'
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        for rec in myrecords:
            print('##########################################################################\
######################')
            print()
            print('----------------'.center(90))
            print('IGDTUW, Kashmere Gate'.center(90))
            print('Report Card'.center(90))
            print('----------------'.center(90))
            print()
            print('Enrollment no.: %4d                   Name:%-15s            Course:%-15s '%(rec[0],rec[1],rec[2]))

            print()
            print('Subject                                                Marks')
            print('--------------------------------------------------------------------------------')
            print('subject1                                 :%9.2f'%rec[3])
            print('subject2                                 :%9.2f'%rec[4])
            print('subject3                                 :%9.2f'%rec[5])
            print('subject4                                 :%9.2f'%rec[6])
            print('subject5                                 :%9.2f'%rec[7])
            print('subject6                                 :%9.2f'%rec[8])
            print('---------------------------------------------------------------------------------')
            print()
            print('TOTAL MARKS:  %9.2f          Percentage:  %9.2f        Grade:  %-5s'%(rec[9],rec[10],rec[12]))
            print()
            print('##########################################################################\
######################')               
            print()
            print()
            input('Press Enter Key for Next Slip....')

    except:
        print('Something went wrong')        

def report_card_particular():
    try:
        adm=input('Enter admission no. of student to get the record card...')
        query="select * from student_record where adm_no="+adm
        mycursor.execute(query)
        rec=mycursor.fetchone()
        c=mycursor.rowcount
        if c>0:
            print('##########################################################################\
######################')
            print()
            print('----------------'.center(90))
            print('IGDTUW, Kashmere Gate'.center(90))
            print('Report Card'.center(90))
            print('----------------'.center(90))
            print()
            print('Enrollment no.: %4d                   Name:%-15s            Course:%-15s '%(rec[0],rec[1],rec[2]))

            print()
            print('Subject                                                Marks')
            print('--------------------------------------------------------------------------------')
            print('subject1                                 :%9.2f'%rec[3])
            print('subject2                                 :%9.2f'%rec[4])
            print('subject3                                 :%9.2f'%rec[5])
            print('subject4                                 :%9.2f'%rec[6])
            print('subject5                                 :%9.2f'%rec[7])
            print('subject6                                 :%9.2f'%rec[8])
            print('---------------------------------------------------------------------------------')
            print()
            print('TOTAL MARKS:  %9.2f                  Percentage:  %9.2f        Grade:  %-5s'%(rec[9],rec[10],rec[12]))
            print()
            print('##########################################################################\
######################')               
            print()
            print()
        else:
            print('Nothing to display')
    except:
        print('Something went wrong')

###############################################################################################
#                                    MAIN PROGRAM                                             #
###############################################################################################
while True:
    choice=menu()
    if choice==1:
        ch1=menu2()
        if ch1==1:
            add_student_record()
        if ch1==2:
            display_all_student_data()
            display_info_table()
        if ch1==3:
            display_part_student_data()
        if ch1==4:
            modify_student_info()
        if ch1==5:
            delete_particular_student_record()
    if choice==2:
        ch1=menu2()
        if ch1==1:
            add_course_details()
        if ch1==2:
            display_all_course_data()
            display_course_table()
        if ch1==3:
            display_part_course_data()
        if ch1==4:
            modify_course_data()
        if ch1==5:
            delete_particular_course_record()
    if choice==3:
        ch1=menu2()
        if ch1==1:
            add_student_score()
        if ch1==2:
            display_all_student_records()
            display_score_table()
        if ch1==3:
            display_part_student_record()
        if ch1==4:
            modify_score_record()
        if ch1==5:
            delete_particular_score_record()
    if choice==4:
        print('1.Display all report cards')
        print('2.Display particulat report card')
        ch2=int(input('enter your choice: '))
        if ch2==1:
            report_card_all()
        if ch2==2:
            report_card_particular()
    if choice==5:
        print('EXITING PROGRAM')
        print('GOODBYE')
        break
