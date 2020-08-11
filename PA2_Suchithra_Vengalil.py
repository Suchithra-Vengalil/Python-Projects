'''
Created on 1/23/2019 @author: TBABAIAN
 
Starting code for hw2. Place the rest of the code below the comment line 

# your code goes here

Created on Feb 2, 2020

@author: suchi

#Inputs

keyWord=input('Enter the keyword:  ')
lineLength=input('Enter the line length: ')

print ('--------------\n')
print('Outputting the sentence followed by the text schema with', 20 , 'characters per line',':') 
print('*****\n')

text=textOrig.lower()
key=keyWord.lower()

 
Created on Feb 3, 2020

@author: suchi


def fromFile(file):    
file = open(file, 'r')
    line = file.read() 
    return line 
txtfile =  input("Please enter the name of the file containing the text: ")
textOrig = fromFile(txtfile).strip() 
print('Contents of file',textOrig\n,txtfile)

keyword=input('Enter the keyword:  ')
linelength=input('Enter the line length: ')
print ('--------------\n')
print('Outputting the sentence followed by the text schema with', lineLength , 'characters per line',':') 
print('*****\n')
#Part 1 Enter the inputs

#For computational purpose
'''
text = "One two three. Four five, six - seven! Eight, nine. Ten eleven twelve. Thirteen fourteen fifteen, Sixteen."
keyword = "thirteen"
linelength = 20 #for schema

keywordupper= keyword.upper()
len_key=len(keyword)

#Replace all ,! or - by period
textOnlyPeriods = text.replace(',', ' ').replace('?', '.').\
        replace('!', '.').replace('-', ' ')
#convert text into lower
newText=textOnlyPeriods.lower()
key=keyword.lower()
#Part1
key_Pos = newText.find(key)#Find the position of keyword
Pos_Period1=newText.find(".")#Find the position of first period
keyWordEndPos=text.find(" ",key_Pos)#Find the key word end position
Pos_Period2=newText.find('.',key_Pos,len(newText))#Find the position of second period

#Conditions to test:#if the keyword appears in the first sentence
if key_Pos <Pos_Period1:
    sentence=text[ :Pos_Period1]#find the first sentence that has the key
    begin=sentence[:key_Pos]#find the beginning of sentence
    end=sentence[keyWordEndPos:]#find the end of sentence
    outputsentence=begin+keywordupper+end#outout joining both beginning and end
    print(outputsentence)
#Conditions to test:#if the keyword appears in the sentence after the first one
else: 
    periodbeforekey=newText.rfind('.',Pos_Period1,key_Pos) #find the position of period before key
    periodafterkey=newText.find('.',keyWordEndPos)#find the position of period after key
    beginsentence=text[periodbeforekey+2:key_Pos]#find the beginning sentence
    endsentence=text[keyWordEndPos:periodafterkey+2]#find the end sentence
    outputsentence2=beginsentence+keywordupper+endsentence # join all sentences
    print(outputsentence2)
#part 2:Find the line length and compute the number of dots
numoflines=len(text)//linelength # get the line length with integer division
numoflinesbeforekeyword=key_Pos//linelength #compute the no of dots
noofdots=(("." * linelength+"\n")*numoflines)#placement of dots equal to length
#create the line with the keyword
remainingdots=len(text) % linelength# get the line length with remainder division
lastlinedots="." * remainingdots
Totaldots=noofdots+lastlinedots
print(Totaldots)
