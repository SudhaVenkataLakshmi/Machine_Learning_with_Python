Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> def fav_color(name,color):
...     print(name+"'s favourite color is"+color+".")
...     fav_color("Sushma","Blue")
... 
...     
>>> 
>>> def fav_color(name,color):
...         print(name+"'s favourite color is"+color+".")
...     fav_color("Sushma","Blue")
... 
SyntaxError: unindent does not match any outer indentation level
>>> def fav_color(name,color):
...             print(name+"'s favourite color is"+color+".")
...             fav_color("Sushma","Blue")
