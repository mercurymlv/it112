import os

# Don't forget proper error-handing!
try:
    with open('Valdez_Resume.txt', 'r') as reader:

        resume = reader.read(-1)
    
        #Reference: https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/
        print('Parsing', reader.name, 'from', os.path.abspath(reader.name))
        
        # Reference: https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/
        # Split by whitespace
        print('Number of Words:', len(resume.split()))
        # use +1 for last line, but check if file is empty
        print('Number of Lines:', resume.count('\n') + (1 if resume else 0))
        print('Number of Characters:',len(resume))

except FileNotFoundError:
    print('File not found!')

except PermissionError:
    print('Permission denied! Unable to open the file.')
