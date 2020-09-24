import boto3
import os
def func1():
    path='C:/Users/KRITU/random/'
    for root,direct,files in os.walk(path):
        #print(root)
        #print(direct)
        #print(files)
        for i in files:
            x=os.path.splitext(i)[-1].lower()
        
            if x== ".pdf": 
                
                s3 = boto3.resource('s3')

                data = open(i, 'rb')
                
                s3.Bucket('kritikasbucket').put_object(Key=i, Body=data)
                print("Success1",i)
            else:
                print("Error",i)
            
def func2():      #manually entering a file to store
    s3 = boto3.resource('s3')

    data = open('KRITIKAreport.pdf ', 'rb')
    s3.Bucket('kritikasbucket1210').put_object(Key='KRITIKAreport.pdf ', Body=data)  
    print("Success2")
func1()
func2()    