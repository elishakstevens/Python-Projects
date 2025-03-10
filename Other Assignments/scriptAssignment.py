
import fnmatch
import os


def absPath():
    relPath = 'C:\\Users\\elish\\OneDrive\\Documents\\GitHub\\Python-Projects\\scriptAssignDir\\'
    for f in os.listdir(relPath):
        if fnmatch.fnmatch(f, '*.txt'):
            abPath = os.path.join(relPath, f)
            mTime = os.path.getmtime(abPath)
            print(f, mTime)



if __name__ == "__main__":
    absPath()
