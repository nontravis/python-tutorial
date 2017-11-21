from __future__ import print_function


#┌─────────────────┐
#│ NOTE: OS module │
#└─────────────────┘
"c:\\spam\\eggs.png"    # windows
print("\\")

"\\".join(["folder1", "folder2", "folder3", "file.png"])

import os
os.path.join("folder1", "folder2", "folder3", "file.png")
os.sep

os.getcwd()
os.chdir("/")

# Absolute ==> from root
# Relative Paths ==> from current directory
os.path.abspath("file.png")
os.path.abspath(os.path.join("..", "..", "file.png"))
os.path.isabs("/")
os.path.isabs("./file.png")

os.path.relpath("/folder1/folder2/file.png", "/folder1")  # second argument = from

os.path.dirname("/folder1/folder2/file.png")
os.path.basename("/folder1/folder2/file.png")
os.path.exists("/folder1/folder2/file.png")

os.path.isfile("/folder1/folder2/file.png")     # if not found return false
os.path.isdir("/folder1/folder2/file.png")      # if not found return false

os.path.getsize("/Users/thekhaeng/.zshrc")      # bytes
os.listdir("/Users")

os.makedirs("/Users/thekhaeng/test_dir")


#┌──────────────────────────┐
#│ NOTE: Read or Write file │
#└──────────────────────────┘

# if not found will auto create file
# default is read mode
f = open(os.path.join(os.getcwd(), "test.txt"))
f = open(os.path.abspath("test.txt"))       # is same
f.read()    # show all content of file
f.seek(0)           # move cursor to the beginning of the file
f.close()    # after we're done reading the file context should call close method

f.readlines()   # return list of line contents
f.close()
# a: append mode writing to end of existing file
# w: write mode will replace old contents
f = open(os.path.join(os.getcwd(), "test2.txt"), 'w')
f.write("Hello world!")
f.close()


import shelve   # look like dictionary
sf = shelve.open("myshelve")
sf["cats"] = ["Zophie", "Pooka", "Simon", "Fat-tail", "Cleo"]
sf.close()

sf = shelve.open("myshelve")
sf["cats"]
list(sf.keys())
sf.values()
sf.close()


#┌────────────────────────────────┐
#│ NOTE: Copy or Move file/folder │
#└────────────────────────────────┘
import shutil

shutil.copy(os.path.abspath("test.txt"),
            os.path.abspath("copyfolder"))
shutil.copy(os.path.abspath("test.txt"),
            os.path.abspath("copyfolder" + os.sep + "renametest.txt"))
shutil.copytree(os.path.abspath("copyfolder"),
                os.path.abspath("backup_copyfolder"))

shutil.move(os.path.abspath("myshelve"), os.path.abspath("copyfolder"))
shutil.move(os.path.abspath("myshelve"), os.path.abspath("copyfolder" + os.sep + "renameshelve"))


#┌──────────────────────────┐
#│ NOTE: Delete file/folder │
#└──────────────────────────┘
import os
os.unlink("delete.txt")     # delete file
os.rmdir("deletefolder")    # delete empty folder only

import shutil
shutil.rmtree("deletefolder")   # delete all item permanent (really be careful)

import send2trash   # NOTE: recommend
send2trash.send2trash("deletefile")     # send any file/folder to recycling bin


#┌────────────────────────────────┐
#│ NOTE: Walking a directory tree │
#└────────────────────────────────┘
import os
for foldername, subfolders, filenames in os.walk("."):
    print("The folder is " + foldername)
    print("The subfolders is " + foldername + " are: " + str(subfolders))
    print("The filenames is " + foldername + " are: " + str(filenames))
    print("")

    # no something
