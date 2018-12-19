import os
directory = 'final'
if not os.path.exists(directory):
    os.makedirs(directory)
    
lwarpFiles = []
dir_list =  os.listdir()
for full_file_name in dir_list:
    base_nameTemp, extensionTemp = os.path.splitext(full_file_name)
    if extensionTemp == '.md': # then .pdf file --> convert to image!
        lwarpFiles.append(full_file_name)
        
import re
for outputFile in lwarpFiles:      
    try:
        base_nameTemp, extensionTemp = os.path.splitext(outputFile)
        finalOutputName = base_nameTemp + extensionTemp
        htmlFile = open(outputFile ,'r',encoding='utf-8')
        htmlSyntaxFile = open(directory + r'/' +finalOutputName,'w',encoding='utf-8')
    except OSError:
        print('Cannot open files, probably because they are being used. \n')
        pass
    # Find number of !!! in line 
    unclosedTags = False 
    for line in htmlFile:

        matches = re.findall(r'!!!', line)
        numMatches = len(matches)
        if numMatches > 0:
            print("The number of matches are:" + numMatches)
        if numMatches == 2:
            newline = re.sub("!!!","~~~admonition",line,1)
            newline = re.sub("!!!","~~~",newline,1)
        elif numMatches == 1:
            if unclosedTags:
                newline = re.sub("!!!","~~~",line, 1)
            else:
                unclosedTags = True
                newline = re.sub("!!!","~~~admonition",line, 1)
        else:
            newline = line
        # newline = re.sub(r'</pre>',r'</code>' + '\n' + r'</pre>' + '\n', newline)
        # account for new problem of <pre class="verbatim" > 
        #newline = re.sub( lwarpCodeVerb,  prismVerbCodeSyn, newline)
        
        htmlSyntaxFile.write(str(newline))
        #print(newline)
    
    htmlFile.close()
    htmlSyntaxFile.close()
print('Script is Done creating files')