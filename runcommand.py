import os
import subprocess
import speech_recognition as sr
import main
from ctypes import *

def commands(choice):
    so_file="run_command.so"
    functions=CDLL(so_file)
    flag=0
    # print("1. List Files")
    # print("2. Shutdown")
    # print("3. List Files Permissions")
    # print("4. List Hidden Files")
    # print("5. Current Working Directory")
    # print("6. Show Date")
    # print("7. Show Day")
    # print("8. Show Time")
    # print("9. Show Calender")
    # print("10. Go to Home Directory")
    # print("11. Go to Root Directory")
    # print("12. Go to User's Directory")
    # print("13. Take Snapshot")
    # print("14. Show Network Status")
    # print("15. Create a file")
    # print("16. Delete a file")
    # print("17. Open Nano Editor")
    # print("18. Open Gedit Editor")
    # print("19. Show Username")
    # print("20. Tell the file type")
    # print("21. Manual of any Command")
    # print("22. Make new Directory")
    # print("23. Login as root")
    # print("24. List Users")
    # print("25. Delete User")
    # print("26. Permanently Delete User")
    # print("27. Add user login")
    # print("28. Who created you?")
    # print("29. Create random file")
    # print("30. Open Visual Code Editor")

    if "list files" in choice:
        if(flag==0):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"ls")
            main.speak_to_speaker("All files in the directory have been listed")
        elif(flag==-1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd /;ls")
            main.speak_to_speaker("All files in the directory have been listed")
        elif(flag==1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd ~;ls")
            main.speak_to_speaker("All files in the directory have been listed")

    elif"shutdown" in choice:
        main.speak_to_speaker("Shutting down")
        functions.shutdown()

    elif"list file permission" in choice:
        if(flag==0):
            functions.multipurpose(b"ls -l")
            main.speak_to_speaker("All files in the directory have been listed with their permissions")
        elif(flag==-1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd /;ls -l")
            main.speak_to_speaker("All files in the directory have been listed with their permissions")
        elif(flag==1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd ~;ls -l")
            main.speak_to_speaker("All files in the directory have been listed with their permissions")

    elif "list hidden files" in choice:
        if(flag==0):
            functions.multipurpose(b"ls -a")
            main.speak_to_speaker("All files in the directory have been listed along with hidden files")
        elif(flag==-1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd /;ls -a")
            main.speak_to_speaker("All files in the directory have been listed along with hidden files")
        elif(flag==1):
            functions.argtypes=[c_char_p]
            functions.multipurpose(b"cd ~;ls -a")
            main.speak_to_speaker("All files in the directory have been listed along with hidden files")

    elif "current working directory" in choice:
        functions.current_directory()
        main.speak_to_speaker("Your current working directory is displayed on the terminal")

    elif "what is the date today"in choice:
        functions.show_date()
        main.speak_to_speaker("today's date has been displayed on the terminal")
    
    elif "what is the day today"in choice:
        functions.show_day()
        main.speak_to_speaker("today's day has been displayed on the terminal")

    elif "what time is it"in choice:
        functions.show_time()
        main.speak_to_speaker("current time has been displayed on the terminal")

    elif "show calendar"in choice:
        functions.show_cal()
        main.speak_to_speaker("the calender has been displayed on the terminal")

    elif "change to home directory"in choice:
        flag=1
        main.speak_to_speaker("changed to home directory")
    
    elif "change to root directory"in choice:
        flag=-1
        main.speak_to_speaker("changed to root directory")

    elif "change to user directory"in choice:
        flag=1
        main.speak_to_speaker("changed to user directory")

    elif "take screenshot"in choice:
        functions.snapshot()
        main.speak_to_speaker("screenshot has been taken")

    elif "show network configuration"in choice:
        functions.network()
        main.speak_to_speaker("network configuration has been displayed on the terminal")

    elif "create a file"in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                fcom="touch "+name
                bcom=bytes(fcom,'utf-8')
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "file is created.")
                print(name + "file is created.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                fcom="cd ~;touch "+name
                bcom=bytes(fcom,'utf-8')
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "file is created.")
                print(name + "file is created.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                fcom="cd /;touch "+name
                bcom=bytes(fcom,'utf-8')
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "file is created.")
                print(name + "file is created.")

    elif "remove a file" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker("Are you sure you want to delete " + name + " ?")
                res1 = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
                name1 = res1["transcription"]
                if "yes" in name1:
                    functions.argtypes=[c_char_p]
                    fcom="rm "+name
                    bcom=bytes(fcom,'utf-8')
                    functions.multipurpose(bcom)
                    print("Sucessfully deleted the file.")
                    main.speak_to_speaker("Sucessfully deleted the file.")
                else:
                    print("You refused to delete the file.")
                    main.speak_to_speaker("Unable to delete the file.")
            else:
                main.speak_to_speaker("Unable to find the file.")
                print("Unable to find the file.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker("Are you sure you want to delete " + name + " ?")
                res1 = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
                name1 = res1["transcription"]
                if "yes" in name1:
                    functions.argtypes=[c_char_p]
                    fcom="cd ~;rm "+name
                    bcom=bytes(fcom,'utf-8')
                    functions.multipurpose(bcom)
                    print("Sucessfully deleted the file.")
                    main.speak_to_speaker("Sucessfully deleted the file.")
                else:
                    print("You refused to delete the file.")
                    main.speak_to_speaker("Unable to delete the file.")
            else:
                main.speak_to_speaker("Unable to find the file.")
                print("Unable to find the file.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            print(res["transcription"])
            name=res["transcription"]
            if(name==None):
                main.speak_to_speaker("could not get file name")
                return
            if os.path.exists(name):
                main.speak_to_speaker("Are you sure you want to delete " + name + " ?")
                res1 = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
                name1 = res1["transcription"]
                if "yes" in name1:
                    functions.argtypes=[c_char_p]
                    fcom="cd /;rm "+name
                    bcom=bytes(fcom,'utf-8')
                    functions.multipurpose(bcom)
                    print("Sucessfully deleted the file.")
                    main.speak_to_speaker("Sucessfully deleted the file.")
                else:
                    print("You refused to delete the file.")
                    main.speak_to_speaker("Unable to delete the file.")
            else:
                main.speak_to_speaker("Unable to find the file.")
                print("Unable to find the file.")

    elif "open nano editor" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="nano "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd ~;nano "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd /;nano "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")

    elif "open gedit editor" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="gedit "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd ~;gedit "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd /;gedit "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")

    elif "who am i" in choice:
        functions.show_user()
        main.speak_to_speaker("your username is displayed on the terminal")
    
    elif "tell the file type" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="file "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd ~;file "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd /;file "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        
    elif "open code editor" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="code "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd ~;code "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            res["transcription"] += ".*"
            name=res["transcription"]
            fcom="cd /;code "+name
            bcom=bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker(name + "file is opened.")

    elif "manual" in choice:
        main.speak_to_speaker("Tell the command name")
        res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        fcom="man "+res["transcription"]
        bcom=bytes(fcom,'utf-8')
        functions.argtypes=[c_char_p]
        functions.multipurpose(bcom)

    elif "make directory" in choice:
        if(flag==0):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            name = str(res["transcription"])
            fcom="mkdir "+name
            bcom=bytes(fcom,'utf-8')
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "directory is created.")
            
        elif(flag==1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            name = str(res["transcription"])
            fcom="cd ~;mkdir "+name
            bcom=bytes(fcom,'utf-8')
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "directory is created.")
        elif(flag==-1):
            main.speak_to_speaker("Tell the file name")
            res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            name = str(res["transcription"])
            fcom="cd /;mkdir "+name
            bcom=bytes(fcom,'utf-8')
            if os.path.exists(name):
                main.speak_to_speaker(name + " already exsists.")
            else:
                functions.argtypes=[c_char_p]
                functions.multipurpose(bcom)
                main.speak_to_speaker(name + "directory is created.")

    elif "login as root" in choice:
        functions.argtypes=[c_char_p]
        functions.multipurpose("sudo -s")
        main.speak_to_speaker("Type your password first")
    
    elif "list users" in choice:
        functions.argtypes=[c_char_p]
        functions.multipurpose("ls /home")
        main.speak_to_speaker("all users have been displayed on the terminal")

    elif "add user" in choice:
        main.speak_to_speaker("Tell the user name")
        res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            main.speak_to_speaker(res["transcription"] + " user already exists.")
            print(res + " user already exists.")
        else:
            fcom = "sudo adduser " + r
            bcom = bytes(fcom,'utf-8')
            functions.argtypes=[c_char_p]
            functions.multipurpose(bcom)
            main.speak_to_speaker("Sucessfully created the user.")
    
    elif "delete user" in choice:
        main.speak_to_speaker("Tell the user name")
        res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + name
        if os.path.exists(r):
            main.speak_to_speaker("Are you sure you want to delete " + res + " ?")
            res1 = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
            if "yes" in res1:
                fcom="sudo deluser "+name
                bcom=bytes(fcom,'utf-8')
                functions.argtypes=[c_char_p]
                functions.multipurpose(bcom)
                main.speak_to_speaker("Sucessfully deleted the user.")
            else:
                print("You refused to delete the user.")
                main.speak_to_speaker("Unable to delete the user.")
        else:
            main.speak_to_speaker(res + " user does not exists.")
            print(res + " user does not exists.")

    # elif "delete user" in choice:
    #     main.speak_to_speaker("Tell the user name")
    #     res = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
    #     name = str(res["transcription"])
    #     r = "/home" + name
    #     if os.path.exists(r):
    #         main.speak_to_speaker("Are you sure you want to delete " + res + " ?")
    #         res1 = main.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
    #         if "yes" in res1:
    #             fcom="sudo deluser "+name+" -remove-home"
    #             bcom=bytes(fcom,'utf-8')
    #             functions.argtypes=[c_char_p]
    #             functions.multipurpose(bcom)
    #             main.speak_to_speaker("Sucessfully deleted the user.")
    #         else:
    #             print("You refused to delete the user.")
    #             main.speak_to_speaker("Unable to delete the user.")
    #     else:
    #         main.speak_to_speaker(res + " user does not exists.")
    #         print(res + " user does not exists.")
    
    elif "create a random file" in choice:
        functions.argtypes=[c_char_p]
        functions.multipurpose("touch -t")

    elif "who created you" in choice:
        main.speak_to_speaker("i am created by hello hadiqa, hello wahaj, an noor baji")
        
    else:
        print("No such command exist.")
        main.speak_to_speaker("No such command exist.")