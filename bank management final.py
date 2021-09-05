import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='9975696628',database='BANK_MANAGEMENT')

def OpenAcc():
    n=input("Enter The Name: ")
    n=n.title()

    ac=input("Enter The Account No: ")
    db=input("Enter The Date of Birth: ")
    add=input("Enter The Address: ")
    # try:
    #     cn=int(input("Enter The Contact Number: "))
    #     cn = str(cn)
    # except:
    #     print("Contact number should be in digits")
    #     cn=input("Enter The Contact Number: ")
    cn=input("Enter The Contact Number: ")
    ob=int(input("Enter The Account Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1='insert into account values (%s,%s,%s,%s,%s,%s)' 
    sql2='insert into amount values (%s,%s,%s)'
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Succesfully")
    main()

def DespoAmo():
    amount= input("Enter the amount you want to deposit: ")
    ac=input("Enter The Account No: ")
    a = 'select balance from amount where Accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a% data)
    result=x.fetchone()
    t=result[0] + int(amount)
    sql=('update amount set Balance=%s where AccNo=%s')
    d=(t,ac)
    x.execute(sql, d) 
    mydb.commit()
    main()

def WithdrawAmount():
    amount=input("Enter the amount you want to withdraw: ")
    ac = input("Enter The Account No: ")
    a='select balance from amount where Accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a%data)
    result=x.fetchone()
    t=result[0]-float(amount)
    sql=('update amount set balance=%s where Accno=%s')
    d=(t,ac)
    x.execute(sql%d) 
    mydb.commit()
    main()

def BalEnq():
    ac=input("Enter the account No: ")
    a='select * from amount where Accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a%data)
    result=x.fetchone()
    print("balance for account:",ac,"is",result[-1])

def DisDetails():
    ac=input("Enter the account No: ")
    a='select * from account where Accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a%data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac=input("Enter account no: ")
    sql1='delete from account where Accno=%s'
    sql2='delete from amount where Accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1%data)
    x.execute(sql2%data)
    mydb.commit()
    main()



    
def main():
    print(''' 
              1.OPEN NEW ACCOUNT
              2.DEPOSIT AMOUNT
              3.WITHDRAW AMOUNT
              4.BALANCE ENQUIRY
              5.DISPLAY CUSTOMER DETAILS
              6.CLOSE AN ACCOUNT
              7.CANCEL''')
choice = 0
while(choice != '7'):
    choice = input("Enter the operation you want to perform : ")
    if (choice=='1'):
        OpenAcc() 
    elif(choice=='2'):
        DespoAmo()  
    elif(choice=='3'):
        WithdrawAmount()   
    elif(choice=='4'):
        BalEnq()
    elif(choice=='5'):
        DisDetails()
    elif(choice=='6'):
        CloseAcc()
    else:
        print("Invalid Choice")