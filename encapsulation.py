# encapsulation is the process of restricting access to methods and variables in a class
# This is done to prevent the data from being modified by accident
# In python, we denote private attributes using underscore as the prefix i.e single _ or double __
# Single underscore means protected attribute
# Double underscore means private attribute
# Protected attributes can be accessed by the class and its sub-classes
# Private attributes can only be accessed by the class itself

from Opp_Proj import chatbook
ed1=chatbook()
print(ed1._fnam)  #obj._attribute
print(ed1._chatbook__name)   #obj._class__attribute

#give me example of these # 
# Single underscore means protected attribute
# Double underscore means private attribute

