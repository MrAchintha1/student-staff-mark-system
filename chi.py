# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID W2051550
# Student ID 20230061 (IIT Sri Lanka) 
# Date 12/13/2023 : 10.00AM

from graphics import *


def saveFile():
    
    with open('saveFile.txt', 'w+') as file:

        # write elements of list
        for items in progressionData:
            file.write('%s\n' % items)
        # display content of the file
        # close the file
    

# looped function for progression outcome
def progressionOutcome():
    # student counters
    global progress, trailer, retriever, excluded  # mark outcome
    global total  # total successful inputs
    global progressionData
    
    progress = trailer = retriever = excluded = 0
    total = 0

    # part -2 list for progression data
    progressionData = []

    # allowed marks
    allowed = [0, 20, 40, 60, 80, 100, 120]

    # condition for work as do while loop
    condition = False
    while True:
        while condition == True:
             
            # student can only enter one valid mark
            if user == "student" and total == 1:
                return
            print("\n"+"Would you like to enter another set of data?")
            rerun = input("Enter 'y' for yes or 'q' to quit and view results: ").lower().strip()
            print()
            if rerun == "y":
                break
            elif rerun == "q":
                return
            else:
                print("invalid option")
        # asks question ignoring first attempt
        condition = True
        try:
            
            passCredits = int(input("Please enter your credits at pass: ").strip())
            if passCredits in allowed:
                pass
            else:
                print("Out of range.")
                # if error found , returns back to 'rerun'
                continue

            defer = int(input("Please enter your credit at defer: ").strip())
            if defer in allowed:
                pass
            else:
                print("Out of range.")
                continue

            fail = int(input("Please enter your credit at fail: ").strip())
            if fail in allowed:
                pass
            else:
                print("Out of range.")
                continue

            # total check
            if passCredits + defer + fail == 120:
                pass
            else:
                print("Total incorrect.")
                continue  # check total is correct , return to question
  
            # progress checking
            if passCredits + defer + fail == 120:
                if passCredits == 120:
                    print("Progress")
                    progress += 1
                    status = "Progress"
                elif passCredits == 100:
                    print("Progress (module trailer)")
                    trailer += 1
                    status = "Progress (module trailer)"
                elif fail >= 80:
                    print("Exclude")
                    excluded += 1
                    status = "Exclude"
                else:
                    print("Do not progress – module retriever")
                    retriever += 1
                    status = "Do not progress – module retriever"
                total += 1
                # string for students progression Data , part 2
                studentStatus = status + " - " + f"{passCredits}" + " ," + f"{defer}" + " ," + f"{fail}"
                progressionData.append(studentStatus)

            else:
                print("Total incorrect.")
                continue

        # if string entered returns back to question
        except ValueError:
            print("Integer required ")
            continue


# histogram function
def histogram():
    # return maximumValue
    maximumValue = max(progress, trailer, retriever, excluded)
    listed = (progress, trailer, retriever, excluded)

    # color list
    colorRed = (174, 160, 166, 209)
    colorGreen = (248, 198, 188, 182)
    colorBlue = (160, 137, 118, 180)

    # window
    win = GraphWin("Histogram", 700, 650)
    win.setBackground(color_rgb(238, 242, 237))

    # heading
    heading = Text(Point(160, 20), "Histogram Results")
    heading.setSize(20)
    heading.draw(win)
    # last line
    totalOutcome = Text(Point(150, 550), f"{total}" + ", outcomes in total")
    totalOutcome.setSize(20)
    totalOutcome.draw(win)

    # x axis
    line = Line(Point(20, 500), Point(550, 500))
    line.setFill("Black")
    line.draw(win)

    wordPoint = 100
    lengthStart = 50
    lengthEnd = 150
    textList = ("Progress", "Trailer", "Retriever", "Excluded")

    for x in range(4):
        rect = Rectangle(Point(lengthStart, 500), Point(lengthEnd, 500 - (listed[x] / maximumValue) * 400))
        rect.setFill(color_rgb(colorRed[x], colorGreen[x], colorBlue[x]))
        rect.setOutline("Black")
        rect.draw(win)

        text = Text(Point(wordPoint, 520), textList[x])
        text.setFill(color_rgb(121, 135, 152))
        text.draw(win)

        mark = Text(Point(wordPoint, 480 - (listed[x] / maximumValue) * 400), f"{listed[x]}")
        mark.draw(win)
        mark.setFill(color_rgb(121, 135, 152))

        # alignment
        wordPoint += 120
        lengthStart += 120
        lengthEnd += 120

    # closing window
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        win.close()


user = input("Please enter 'student' or 'staff'-  ").lower().strip()
print()
if user == "student":
    # student attempt does not go to record
    # student should allow one correct attempt
    progressionOutcome()

elif user == "staff":
    progressionOutcome()
    histogram()
    # part 2 progression display
    print("\n" + "Part2 \n")
    if total > 0:
        for i in range(total):
            print(progressionData[i])
            saveFile()
        print("\n"+"part3\n")  # outcome
        file = open('saveFile.txt', 'r')
        print(file.read())
        print("File written successfully")
        file.close()

else:
    print("Invalid input" + "\n" + "Program will exit.")
    sys.exit()
