import os,time,shutil
p = input("Enter the path you want to delete:")  #Enter the new folder path,if you want put path of any other folder do at your own risk 
exist = os.path.exists(p)
if(exist == True):
    y = os.stat(p).st_ctime
    print(y)
    t =  time.time()
    print(t)
    c = t-y
    print(c)

    while (True):
        isFile = os.path.isfile(p)
        
        if ((time.time()-t)>=60):     #since, we cannot wait for 30 days so it will be deletd after 60 sec but if you wnat to use it for 30 days put 2592000 instead of 60
            if(isFile==True):
                os.remove(p)
                print("file deleted succesfully")
            else:
                shutil.rmtree(p)
                print("folder deleted succesfully")
            break
else:
    print("Path does not exist")
