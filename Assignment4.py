'''
Created on Mar 26, 2020

@author: suchi
'''
import os.path
def processProgramFile(programFilePath):
    '''This function will be used to read information about programs and stores it in a easy accessible form(as dictionary)
        for retrieval.
    Parameters: 
        programFilePath - A single parameter of type string, providing the path to a program description file
    Returns:
        A tuple consisting of the program name and the created dictionary
    '''
    data_dict={}
    with open(programFilePath,'r') as datafile:
        certProgName = datafile.readline()
        
        for line in datafile:
            dataLine1=line.split(maxsplit=1)
            if dataLine1[1].strip().endswith('.'):
                data_dict[dataLine1[0]]=dataLine1[1].strip()
            else:
                data_dict[dataLine1[0]]=dataLine1[1].strip()+'.'
        return certProgName,data_dict

def processPrereqsFile(prereqFilePath):
    ''' This function will be used to read information about the prerequisites structure and stores it in a easy accessible 
    form (as dictionary) for retrieval
    Parameters: 
        prereqFilePath - A single parameter of type string, providing the path to a file defining prerequisites.
    Returns:
        prereq_dict-The constructed dictionary of prerequisites 
    '''
    with open(prereqFilePath,'r') as prereqcoursefile:
        #create a dictionary of all the prerequisite courses
        prereq_dict={}
        for line in prereqcoursefile:
            prereqLine1=line.split(':',1)
            prereqlst=prereqLine1[1].split()
            prereq_dict[prereqLine1[0]]= tuple(prereqlst)
    
    return prereq_dict        

def processClassFiles(classListfolder):
    ''' :This function will help in combining the data about enrollments into courses from multiple files into a 
    single dictionary organized by course number
    Parameters: 
        classListfolder - A single parameter, defining the sub folder with the class list files, as outlined in the Data section
    Returns:
        The constructed dictionary with the list of students who have taken or are taking the course 
    '''
    
    enrolledStudents={}
    classList=os.listdir(os.path.join(os.getcwd(),classListfolder))
    
    for classFilename in classList:
       #Opening the enrolled course file
        with open(os.path.join(os.getcwd(),classListfolder,classFilename)) as enrollCourseFile:
            
            firstletter = enrollCourseFile.read(1)
            courseNumber = enrollCourseFile.read(4)
            enrollCourseFile.readline()
            #checking the course file
            if firstletter =='c' and courseNumber.isdigit():
                #creating a new key when course not found in the enrolledStudents dictionary
                if courseNumber not in enrolledStudents: 
                    enrolledStudents[courseNumber]=set()
                    
                for line in enrollCourseFile:                    
                    enrollLstLine1=line.split()
                    (enrolledStudents.get(courseNumber)).add(enrollLstLine1[0]) 
                    
    return enrolledStudents              

def initFromFiles(subFolder):
    ''' This function will create data structures with the information that is currently available in files by calling the 
    functions identified above
    Parameters: 
        subFolder -  A single parameter, defining the sub folder with the files
    Returns:
           A tuple with the constructed dictionaries for program courses,class lists and prerequisites. 
    '''
    #call the previous functions to get the 2 certificate course details in the file within the subfolders 
    certCourse1,certCourse1_dict =processProgramFile(os.path.join(os.getcwd(),subFolder,'program1.txt'))

    certCourse2,certCourse2_dict =processProgramFile(os.path.join(os.getcwd(),subFolder,'program2.txt'))
    
    #creating a consolidated dictionary
    data_dict=certCourse1_dict
    
    for key in certCourse2_dict.keys():
        if key not in data_dict:
            data_dict[key]=certCourse2_dict[key]
            
    #call the processPrereqsFile function to get prerequisite course details        
    prereq_dict=processPrereqsFile(os.path.join(os.getcwd(),subFolder,'prereqs.txt'))
    
    #call the processClassFiles function to get enrolled student details 
    class_dict=processClassFiles(subFolder)
    
    return data_dict,class_dict,prereq_dict

def estimateClass(courseNumber,data_dict,class_dict,prereq_dict):
    ''' This function will be used to find a list of eligible students for a given class
        courseNumber- Will ask the user for a course number and the program will output the number of eligible students for that course
        data_dict - A consolidated dictionary of all courses from all programs
        class_dict -A list of students enrolled in a class with courseNumber as key 
        prereq_dict-Earlier created dictionary of all the prerequisite courses
    Returns:
        A sorted list of students who would be eligible to take the course, specified by the parameter,
        in the next semester
    '''
    eligibleStudentsdtList=set()
    
    if courseNumber in data_dict.keys():
        #creating a consolidated student list 
        for studentName in class_dict.values():
            eligibleStudentsdtList = eligibleStudentsdtList.union(studentName)
        
        #Finding the difference of students who have previously taken the course from the total list
        eligibleStudentsdtList = eligibleStudentsdtList.difference(class_dict[courseNumber])
        
        #check if the prerequisite course criterion is fulfilled and making the final list of eligible students
        
        if courseNumber in prereq_dict.keys():
            for prereq in prereq_dict[courseNumber]:
                eligibleStudentsdtList = eligibleStudentsdtList.intersection(class_dict[prereq])
        sortedListEligible=sorted(eligibleStudentsdtList)       
        
        return list(sortedListEligible)
        
        
    else:
        return list(set())

def main():
    '''function used to get the user to input sub folder name and course code
    parameter: Nil
    Returns: Nil
    '''
    #user inputs the sub folder name
    subFolder=input('Please enter the name of the subfolder with files:')
    
    data_dict, class_dict, prereq_dict=initFromFiles(subFolder)
    
    courseNumber=0
    while(courseNumber != ''):
            courseNumber=input('Enter course number or press enter to stop:')#user inputs the course code
            if courseNumber.isdigit():
                eligiblestudentslst=estimateClass(courseNumber,data_dict,class_dict,prereq_dict)
                if courseNumber in data_dict.keys():
                    print('There are', len(eligiblestudentslst),'students who could take course',courseNumber,data_dict[courseNumber])
                else:
                    print('There are', len(eligiblestudentslst),'students who could take course',courseNumber,'None')
                    
                
                                      
                                    
                    
                
main()
