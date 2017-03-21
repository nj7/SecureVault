import shutil
import os
import bat_exe


def main():

    #taking user input of view a file or adding a file to vault
    #choice = takeInput()    

    file_path=raw_input("Enter File Path\n")
    file_name=raw_input("Enter File Name\n")
    src_of_file = file_path+"\\"
    src_of_file += file_name

    print "The Source of File is :: "+ src_of_file

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
        print "Congrats this is first run \nDierectory created succesfully"

    # copy file file from location to secure vault
    shutil.copy2(src_of_file, dierectory)

    #remove file from location
    os.remove(src_of_file)

    #creating batch file to execute
    dierectory += "\\batch.bat"
    batch_file = open(dierectory,"w+")
    batch_file.write("C:\ncd C:\Secure_nj_project\nattrib +h +r +s "+vault+"\necho y|cacls "+vault+" /p everyone:n")
    batch_file.close

def takeInput():
    choice = 10
    while(choice != '1' or choice != '2'):
        choice = raw_input("Select an option \n1.Open a file  \n2.Add file to vault\n")
        choice = int(choice)
    return choice

    
if  __name__ =='__main__':
    main()
    #executing Batch File
    bat_exe.open_batch()
