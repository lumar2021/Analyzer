import nltk

first_structure = """ 
E -> E '+' T | T
T -> T '*' F | F
F -> '(' E ')' | 'digit'
"""

second_structure =  """
S -> 'a' B D 'h'
B -> 'c' C
C -> 'b' C | 
D -> E F
E -> 'g'| 
F -> 'f'| 
"""

third_structure = """
S -> '(' L ')' | 'a'
L -> S M 
M -> ',' S M| 
"""

fourth_structure = """
S -> '1' S | '0' T | 
T -> '1' T | '0' S
"""

fifth_structure = """ 
A -> 'a' B E
E -> 'd' E | 
B -> 'b'
C -> 'g'
"""

while True:
    stay = int(input("If you want to continue press any number other than 0: "))
    if stay == 0:
        break
    grammar = int(input("Enter the number corresponding to the grammar: "))
  

    if grammar == 1:
        analysis = nltk.ChartParser(nltk.CFG.fromstring(first_structure))
    elif grammar ==2:
        analysis = nltk.ChartParser(nltk.CFG.fromstring(second_structure))
    elif grammar == 3:
        analysis = nltk.ChartParser(nltk.CFG.fromstring(third_structure))
    elif grammar == 4:
        analysis = nltk.ChartParser(nltk.CFG.fromstring(fourth_structure))
    elif grammar == 5:
        analysis = nltk.ChartParser(nltk.CFG.fromstring(fifth_structure))
  
    txt=""
    print("-------------------------------")
    word = input("Enter the text to analyze: ")
    try:      
        for letter in analysis.parse(word.split()):
            if letter:
                txt +="Valid phrase"

        if txt ==  "":
            print("Invalid phrase")
        else:
            print(txt)
    except ValueError as e:
        print(e)
    
      
    print("-------------------------------")