"""
String Mirror
Given a string, return a new string that consists of the given string 
with a reversed copy of itself appended to the end of it.
"""

def mirror(s):
    string_s = s
    for i in s[::-1]:
        string_s += i

    return string_s

