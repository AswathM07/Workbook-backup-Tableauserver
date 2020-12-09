import boto3
import os
import tableauserverclient as TSC
import getpass
import datetime
import shutil
today = datetime.datetime.now()

def main():
    p=input("Enter your path to create folder")
    if today.hour < 12:
        h = "00"
    else:
        h = "12"

    s=p+today.strftime('%d_%m_%Y')
    os.mkdir(s)
    try:
        k=today-datetime.timedelta(days=3)
        shutil.rmtree(p+k.strftime('%d_%m_%Y'))
    except:
        pass	
    return(s)
   
    

if __name__ == '__main__':
    s=main()
	
        #tableau workbook download

    un=input("Enter usrer name ")
    ps=getpass.getpass("Enter password ")
    surl=input("Enter the Server Url")
    #sn=input("Enter site name ")
	
    tableau_auth = TSC.TableauAuth(un, ps)
    
	# or for a personal access token
    #tableau_auth = TSC.PersonalAccessTokenAuth(, 'TOKEN_VALUE', 'SITENAME')
	#'https://10ax.online.tableau.com' this is for online 
    server = TSC.Server(surl)
    server.auth.sign_in(tableau_auth)
	 #Create an interval to run every 2 hours between 2:30AM and 11:00PM
	 #print names of first 100 workbooks
    all_workbooks_items, pagination_item = server.workbooks.get()
    for i in all_workbooks_items:
        k=i.id
        n=i.name
        file_path = server.workbooks.download(k)
        s3 = boto3.client('s3')
        s3.upload_file(file_path,'workbook-backup',file_path)
        shutil.move(file_path, s+'/'+file_path.split("\\")[-1])	
        print("\nDownloaded the file to {0}.".format(s+'/'+file_path.split("\\")[-1]))