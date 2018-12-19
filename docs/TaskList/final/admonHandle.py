import os
    
lwarpFiles = []
dir_list =  os.listdir()
for full_file_name in dir_list:
    base_nameTemp, extensionTemp = os.path.splitext(full_file_name)
    if extensionTemp == '.tex': # then .pdf file --> convert to image!
        lwarpFiles.append(full_file_name)
        
import re
for outputFile in lwarpFiles:      
    try:
        base_nameTemp, extensionTemp = os.path.splitext(outputFile)
        finalOutputName = base_nameTemp + extensionTemp
        htmlFile = open(outputFile ,'r',encoding='utf-8', errors='replace')
        htmlSyntaxFile = open(base_nameTemp + 'cool_.tex','w',encoding='utf-8', errors='ignore')
    except OSError:
        print('Cannot open files, probably because they are being used. \n')
        pass
    # Find number of !!! in line 
    unclosedTags = False 
    for line in htmlFile:

        matches = re.findall(r'!!!', line)
        numMatches = len(matches)
        if numMatches > 0:
            print("The number of matches are: " + str(numMatches))
        if numMatches == 2:
            newline = re.sub("!!!",'\begin{mdframed}',line,1)
            newline = re.sub("!!!","\end{mdframed}",newline,1)
        elif numMatches == 1:
            if unclosedTags:
                newline = re.sub("!!!",r"\begin{framed}",line)
                unclosedTags = False 
            else:
                unclosedTags = True
                newline = re.sub("!!!",r'\end{framed}',line)
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