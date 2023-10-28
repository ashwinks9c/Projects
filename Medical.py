import mysql.connector as db
con=db.connect(host='localhost',user='root',password='football001',database='medical_info')
###################################### Funtions avaialable in the program ##################################
# 1. fn_list_hospitals , This function will return the list of all hospitals 
# 2. fn_list_doctors , This fucntion will return the list of all doctors
# 3. fn_list_patients , This function will return the list of all patients
# 4. fn_list_medicines , This function will return the list of all medicines


def fn_list_hospitals():#This function will return the list of all hospitals  
    try:
        cur=con.cursor()
        query="select * from hospital"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        #con.close()
    except Exception as e:
        print(e)
    except ValueError:
        print("Please enter the specified value")

def fn_list_doctors():#This function will return the list of doctors
    try:
        cur=con.cursor()
        query="select * from doctors"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        #con.close()
    except Exception as e:
        print(e)
    except ValueError:
        print("Please enter the specified value")

def fn_list_patients():#This function will return list of patients
    try:
        cur=con.cursor()
        query="select * from patient"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        #con.close()
    except Exception as e:
        print(e)
    except ValueError:
        print("Please enter the specified value")

def fn_list_medicines():#This function will return list of medicines
    try:
        cur=con.cursor()
        query="select * from medicine"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        #con.close()
    except Exception as e:
        print(e)
    except ValueError:
        print("Please enter the specified value")

def fn_login():
    user=input("Enter username: ")
    passw=input("Enter password: ")
    t=(user,passw)
    cur=con.cursor()
    query="select * from login"
    result=cur.fecthall()
    for i in result:
        if i==t:
            continue
    cur.close()
        



####################################### MAIN PROGRAM ########################################



while True:
    print()
    print("MAIN MENU.....")
    print("1. List of hospitals[press-H]")
    print("2. List of doctors[press-D]")
    print("3. List of patients[press-P]")
    print("4. List of medicines[Press-M]")
    print("5. EXIT[Press-E]")
    print()
    ch=input("Please enter your choice: ")
    print()
    try:
        if ch in'Hh1':
            fn_list_hospitals()
        
        elif ch in'Dd2':    
            fn_list_doctors()
        
        elif ch in'Pp3': 
            fn_list_patients()
        
        elif ch in'Mm4':
            fn_list_medicines()

        elif ch in'Ee5':
                print("Exiting the program")
                break
        
        else:
            print("Please enter the specified value")
               

    except Exception as e:
        print("Check connection string")
    except ValueError:
        print("Please enter the specified value")

print("Thank you...")
con.close()
