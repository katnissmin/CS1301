"""
Georgia Institute of Technology - CS1301
HW09 -  Recursion
"""
#########################################
"""
Function Name: hoursWorked()
Parameters: clockedHours (list)
Returns:  totalHours (int)
"""
def hoursWorked(clockedHours):
    answer = 0
    m = len(clockedHours)
    if m == 0:
        return answer
    else:
        return clockedHours[0] + hoursWorked(clockedHours[1:])
#########################################
"""
Function Name: secretLocation()
Parameters: location (str)
Returns: decodedLocation (str)
"""
def secretLocation(location):
    if len(location) == 0:
        return ""
    if location[0] == " " or location[0].islower() or location[0] == "":
        return location[0] + secretLocation(location[1:])
    else:
        return secretLocation(location[1:])
#########################################
"""
Function Name: springRegistration()
Parameters: originalCRNs (list)
Returns: finalCRNs (list)
"""
def springRegistration(originalCRNs):
    answer = []
    if originalCRNs == []:
        answer = []
    else:
        if (originalCRNs[0] not in originalCRNs[1:]):
            answer = [originalCRNs[0]] + springRegistration(originalCRNs[1:])
        else:
            answer = springRegistration(originalCRNs[1:])
    return answer
#########################################
"""
Function Name: poncePlanner()
Parameters: restaurantChoices (list)
Returns: taFavorites (dict)
"""
def poncePlanner(restaurantChoice):
    adict = {}
    if len(restaurantChoice) == 0:
        return adict
    else:
        adict = poncePlanner(restaurantChoice[1:])
        if restaurantChoice[0][0] not in adict.keys():
            adict[restaurantChoice[0][0]] = restaurantChoice[0][1]
    return adict
#########################################
"""
Function Name: drawRectangle()
Parameters: width (int), height (int)
Returns:  None (NoneType)
"""
def drawRectangle(width, height):
    if width < 3:
        print("You're cutting corners!")
        return
    if height == 0:
        return
    else:
        if width == height or height == 1:
            print("*" * width)
            return drawRectangle(width, height - 1)
        else:
            print("*" + " " * (width-2) + "*")
            return drawRectangle(width, height - 1)
