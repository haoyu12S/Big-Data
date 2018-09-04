# Hands on 1
# Haoyu Shi
# 9/2/2018


import numpy as np


class Scoresheet:
    """

    Get a student sheet using this class

    Attribute:
        classname: Get all class name string list
        studentname: String list about student names
        grades: [len(studentname) x len(classname)] int array

    """
    def __init__(self, classname, studentname, grades):
        """Init attributes to class"""
        self.classname = classname
        self.studentname = studentname
        self.grades = grades
        self.gradesABC = calcABC(grades)
        self.gradesGPA = calcGPA(self.gradesABC)

    def diaplay(self):
        for index in range(len(studentname)):
            print(
                'student name: {}, in these classes {} get {} '
                'respectively.'.format(
                    studentname[index],
                    classname,
                    self.gradesABC[index]))

    def displayGPA(self):

        for index in range(len(studentname)):
            print(
                'student name: {}, GPA is {}.'.format(
                    studentname[index],
                    self.gradesGPA[index]))

    def displayhigh(self):
        ece595 = grades[:, 0]
        ece547 = grades[:, 1]
        ece354 = grades[:, 2]
        index595 = np.argmax(ece595)
        index547 = np.argmax(ece547)
        index354 = np.argmax(ece354)

        print('In {}, the high score and the scorer are {}, {}.\n'
              'In {}, the high score and the scorer are {}, {}.\n'
              'In {}, the high score and the scorer are {}, {}.\n'.format(
                  classname[0], ece595[index595], studentname[int(index595)],
                  classname[1], ece547[index547], studentname[int(index547)],
                  classname[2], ece354[index354], studentname[int(index354)],
              ))


def calcABC(grades):
    """
    Transfer 100 grades to A or B or C etc

    Args:
        grades: [len(studentname) x len(classname)] int array.

    Returns:

    """
    ABCgrade = []
    # print(grades)
    for i in grades:
        # print(i)
        if i >= 90:
            ABCgrade.append('A')
        elif i >= 80:
            ABCgrade.append('B')
        elif i >= 70:
            ABCgrade.append('C')
        elif i >= 60:
            ABCgrade.append('D')
        else:
            ABCgrade.append('F')

    ABC = np.array(ABCgrade)
    ABC.resize(int(len(grades) / 3), 3)

    return ABC


def calcGPA(ABC):
    """
    Get GPA for each student.

    Args:
        ABC: Output from upper function.

    Returns: [len(studentname) x 1]

    """
    GPA = []
    for single in ABC:
        tmp = []
        for grade in single:
            if grade == 'A':
                tmp.append(4)
            elif grade >= 'B':
                tmp.append(3)
            elif grade >= 'C':
                tmp.append(2)
            elif grade >= 'D':
                tmp.append(1)
            else:
                tmp.append(0)
        GPA.append(round(sum(tmp)/3, 2))

    GPA = np.array(GPA)
    GPA.resize((len(GPA)))
    return GPA


def readallinformation(filename):
    with open(filename, 'r') as file:
        information = []
        for line in file.readlines():
            line = line.strip()
            if line != '':
                information.append(line)

        classname = information[0].split(',')[1:]

        studentinformation = information[1:]

        studentname = []
        studentgrade = []
        for student in studentinformation:
            tmp = student.split(',')
            studentname.append(tmp[0])
            studentgrade.append(tmp[1:])

        grades = []
        for i in studentgrade:
            for j in i:
                grades.append(int(j))

        grades = np.array(grades)

        return classname, studentname, grades


def pause():
    programPause = input("Press the <ENTER> key to continue...")


if __name__ == '__main__':
    classname, studentname, grades = readallinformation('records.txt')
    scoresheet = Scoresheet(classname, studentname, grades)

    while (True):
        print('Enter the function index: \n'
              '1. Display all information about score sheet.\n'
              '2. Display the highest score and scorer in each subject.\n'
              '3. Display student GPA.\n'
              '4. Quit.\n')

        index = input('please input index:')
        if index.isdigit():
            index = int(index)
            if 0 < index < 5:
                if index == 1:
                    print('All information about score sheet:')
                    scoresheet.diaplay()
                    pause()
                    print('\n\n')
                elif index == 2:
                    print('The highest score and scorer in each subject:')
                    scoresheet.displayhigh()
                    pause()
                    print('\n\n')
                elif index == 3:
                    print('Student GPA:')
                    scoresheet.displayGPA()
                    pause()
                    print('\n\n')
                else:
                    print("Finished!")
                    break
        else:
            print('Wrong input!! Please input correct number(1~4).\n')
