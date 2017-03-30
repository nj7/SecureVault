import shutil
import os
import batchExecute


def main():

    """taking user input of view a file or adding a file to vault"""
    while True:
        choice = takeInput()

        if choice == 1:
            hideFile()
        elif choice == 2:
            findFile()
        else:
            print "Please Select Correct Output"
        break

    


def takeInput():
    while (True):
        choice = int(raw_input("Select an option \n1.Hide a file  \n2.Unhide a file\n"))
        if choice == 1 or choice == 2:
            return choice

def hideFile():

    while(True):
        file_path=raw_input("Enter File Path\n")
        file_name=raw_input("Enter File Name\n")
        src_of_file = file_path+"\\"
        src_of_file += file_name
        
        print "The Source of File you want to Secure :: "+ src_of_file
        if raw_input("Do you want to Continue (Y/N)") == 'Y' or 'y':
            break
    

    #secure vault source
    vault = "nj$SeCureVaUlt@ThIsIsTeStIngPhAse4ME"
    dierectory = "C:\Secure_nj_project"

    #creating secure vault for first run
    if not os.path.exists(dierectory):
        os.makedirs(dierectory)

    dierectory += "\\"
    dierectory += vault
    if not os.path.exists(dierectory):
        os.makedirs(dierectory)
        print "true"

    # copy file file from location to secure vault
    shutil.copy2(src_of_file, dierectory)

    #remove file from location
    os.remove(src_of_file)

    """Hiding vault having file"""
    
    #creating batch file to hide vault
    dierectory += "\\batch.bat"
    batch_file = open(dierectory,"w+")
    batch_file.write("C:\ncd C:\Secure_nj_project\nattrib +h +r +s "+vault+"\necho y|cacls "+vault+" /p everyone:n")
    batch_file.close()
    
    #executing Batch File
    batchExecute.open_batch(dierectory)



    """Hiding Project Folder having vault"""
    
    #hiding Vault folder
    batch_file = open("C:\\System.bat","w+")
    batch_file.write("C:\nattrib +h +r +s Secure_nj_project\necho y|cacls Secure_nj_project /p everyone:n")
    batch_file.close()
    
    #executing Batch File
    batchExecute.open_batch("C:\\System.bat")



def findFile():

    while(True):
        file_name=raw_input("Enter File Name\n")
        
        print "The Source of File you want to find :: "+ file_name
        if raw_input("Do you want to Continue (Y/N)") == 'Y' or 'y':
            break
    

    #secure vault source
    vault = "nj$SeCureVaUlt@ThIsIsTeStIngPhAse4ME"
    dierectory = "C:\Secure_nj_project"

    #creating secure vault for first run
    if not os.path.exists(dierectory):
        os.makedirs(dierectory)


    if not os.path.exists(dierectory + "\\"+ vault):
        os.makedirs(dierectory)



    """UnHiding Project Folder having vault
    
    #hiding Vault folder
    batch_file = open("C:\\System.bat","w+")
    batch_file.write("C:\necho y|cacls Secure_nj_project /p everyone:f\nattrib -h -r -s Secure_nj_project")
    batch_file.close()
    
    #executing Batch File
    batchExecute.open_batch("C:\\System.bat")"""

    """UnHiding vault having file"""
    
    #creating batch file to hide vault
    batch_file = open(dierectory + "\\batch.bat","w+")
    batch_file.write("C:\ncd C:\Secure_nj_project\necho y|cacls "+vault+" /p everyone:f\nattrib -h -r -s "+vault+"\n")
    batch_file.close()
    
    #executing Batch File
    batchExecute.open_batch(dierectory + "\\batch.bat")

    for file in os.listdir(dierectory +"\\"+vault):
        if file == file_name:
            shutil.copy2(dierectory +"\\"+vault + "\\" + file, "C:\\Users\\nirmit\\Desktop")
    








    
if  __name__ =='__main__':
    main()
