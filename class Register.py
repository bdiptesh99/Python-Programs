import array as n
import math
import os
import sys


print("This is an application Created by Diptesh Banerjee.\nThis application is a register for S3.\n")
print("In q=1 you will get the total list of students.\nIn q=2 you can fine any student bu his serial number.")
q=int(input("Enter Function Number q= "))
x= ['Hmm! OK TRY AGAIN(:))', 'A SAI SRUJAN', 'ABEL SAM THOMAS', 'ADITIYA ANAND MADIHALLI',
    'AJITESH KUMAR', 'AKASH ANAND BURKHE', 'AMOGH MANIKKUWAR', 'ASHEESH CHAUHAN', 'ATHUL SHANKAR', 'B MADHAN',
    'CHINTHA ANUTEJASWINI', 'CYRAC TALUS', 'DIKSHA NEGI', 'GANESH S', 'GUHAN SIDHARTH M', 'JOKESHWARAN RAMESH',
    'KUNDETI VAMSI', 'MOHAMMED KAIF SIDDIQUE', 'NITISH KUMAR D KATTIMANI', 'PRANJAL JAT', 'RAJAT CHAUDHARY',
    'RITESH RANJAN', 'RITVIKA RAVIKUMAR BOLUGUDDE', 'SARANSH BHADUKA', 'TUTA NAVEEN KUMAR',
    'VAISHNAVI PRAKASH KALGUTKAR', 'ABHISHEK RAO R', 'AMAN', 'ANEES ANWAR', 'BHUPESH KUMAR GOSWAMI', 'BRINDA V S',
    'D RAGHAVI', 'DEEPAL T N', 'DEVANSHU VERMA', 'DEVINA KANT', 'G GAUTAM', 'GAYATRI SATISH GUNDAWAR', 'JARUPULA SUNIL',
    'KUHU SUNGH', 'MONAL SINGH', 'NIKAM PRATHAMESH VIJAY', 'NITISH KUMAR GUPTA','PRASHANT','RAM P NAIR',
    'REEVE ROCKY DSOUZA','SHILPASHREE V','SUMANTH N HEGDE','T N MANGUNATH','YASHEANT SINGH SISIDIYA',
    'ABHISHEK CHAVAN','AKSHAY KUMAR R','ANANYA P','CHINTHANASHREE C','DIPTESH DIPTEN BANERJEE',
    'DIVYA','ISHAN BHATTACHARYA','JALAJ AGARWAL','KANCHARLA SNEHITH BHAGAVAN','KUMAR UTKARSH UDESHWAR',
    'MOHIT CHAUHARY','MUDE DAVAN KUMAR NAIK','NANDITA CHOUHAN','NITHIN S','PAWASKAR ATHARVA ASHISH',
    'PRASANNA SARKAR','PRATHAM N','PRIYANSHU KHEMARIYA','REBAKA SAI MANI PRADEEP','S SRIRAM','SANDEEP S T','SANGAY C HEGDE','SHIVANSH JOSHI','STAVAN KUDCHE','TANMAY N RAO','UTKARSH JHA','VIJAY PRABHU K B']
e= len(x)
while q<=3:
    if q==1:
        print("This Is The List of Students\n")
        for i in range(1,e):
            print(x[i])
    if q==2:
        r=int(input("The Serial Number of Student= "))
        while r<e:
            print(x[r])
            break
    break
else:
    print('ok')



input('press ENTER to exit')









