import os
import tableauserverclient as TSC
import getpass
def main():
    
    #print("Current Working Directory " , os.getcwd())
    
    
    try:
        # Change the current working Directory    
        path=input("Enter your path to download workbook")
        os.chdir(path)
        #print("Directory changed")
    except OSError:
        print("Can't change the Current Working Directory")        
    #print("Current Working Directory " , os.getcwd())
    
    # Check if New path exists
    if os.path.exists(path) :
        # Change the current working Directory    
        os.chdir(path)
    else:
        print("Can't change the Current Working Directory")    
        
    
    #print("Current Working Directory " , os.getcwd()) 



        
    
    #print("Current Working Directory " , os.getcwd())
    
if __name__ == '__main__':
    main()
        #tableau workbook download

    un=input("Enter usrer name ")
    ps=input("Enter password ")
    surl=input("Enter the Server Url")
    #sn=input("Enter site name ")
	
    tableau_auth = TSC.TableauAuth(un, ps, sn)

	# or for a personal access token
	# tableau_auth = TSC.PersonalAccessTokenAuth('TOKEN_NAME', 'TOKEN_VALUE', 'SITENAME')
	#'https://10ax.online.tableau.com' this is for online 
    server = TSC.Server(surl)
    server.auth.sign_in(tableau_auth)
	# Create an interval to run every 2 hours between 2:30AM and 11:00PM
	# print names of first 100 workbooks
    all_workbooks_items, pagination_item = server.workbooks.get()
    for i in all_workbooks_items:
        k=i.id
        file_path = server.workbooks.download(k)
        print("\nDownloaded the file to {0}.".format(file_path))