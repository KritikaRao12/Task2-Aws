#importing libraries
import boto3
import os

class Upload_files:

    def __init__(self):           
        pass
        
    def function_upload(self): 
        try:
            path=os.getcwd()    # fetch the current working directory
            for root,directory,files in os.walk(path):
                for file_name in files:
                    file=os.path.splitext(file_name)[-1].lower()               
                    if file== ".pdf":                        # only pdf files
                        s3 = boto3.resource('s3')
                        data = open(file_name, 'rb')
                        s3.Bucket('kritikasbucket').put_object(Key=file_name, Body=data)
                        print("The pdf file "+file_name+ " is uploaded successfully")
                    else:
                        print("Sorry the file "+file_name+ " is not a pdf file")    # other than pdf files
        except Exception as e:                        # if there are no files in the location
            print("Error Code: ",e)           
        return 
       
    def function_specific_upload(self):      # manually entering a file to upload
        try:
            s3 = boto3.resource('s3')
            data = open('KRITIKAreport.pdf ', 'rb')
            s3.Bucket('kritikasbucket1210').put_object(Key='KRITIKAreport.pdf', Body=data)  
            print("The pdf file is uploaded successfully")
        except Exception as e:                # no such file     
            print("Error Code: ",e)      
        return
        
if __name__=="__main__":        
    object_1=Upload_files()    # object creation
    print("Function 1")
    object_1.function_upload()  # call to function 1
    print("- - - - - - - - - - - -")
    print("Function 2")
    object_1.function_specific_upload()   # call to function 2