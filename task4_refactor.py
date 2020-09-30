# importing libraries
import boto3
import logging
import PyPDF2
from botocore.exceptions import ClientError


class Upload_files:

    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_file(self):
        try:
            with open("abd.pdf", 'rb') as data:
                PyPDF2.PdfFileReader(data)
                self.s3.upload_fileobj(data, "kritikasbucket", "d")
                print("The pdf file is uploaded successfully")
        except PyPDF2.utils.PdfReadError:
            print("invalid PDF file")
        except ClientError as e:
            logging.error(e)
            return False
        except IOError as e:
            print("File Not Found")
        except Exception as e:
            print("Error Code:", e)
        return True


if __name__ == "__main__":

    object_1 = Upload_files()    # object creation
    object_1.upload_file()
