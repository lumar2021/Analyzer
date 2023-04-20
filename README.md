# Analyzer


This code was made with NLTK (Natural Language Toolkit) which is a widely used Python library for natural language processing. It provides a wide variety of tools and resources for the analysis and manipulation of natural language text.

The code has three pre-established grammars and numbered from 1 to 5, first you enter a number to know if you want to continue entering more words (if you want to close the cycle enter 0), after this the grammar to be analyzed is requested, you must put the value from 1 to 5 where the menu is as follows:

1. 
E -> E '+' T | T

T -> T '*' F | F

F -> '(' E ')' | 'digit'

2. 
S -> 'a' B D 'h'

B -> 'c' C

C -> 'b' C | 

D -> E F

E -> 'g'| 

F -> 'f'| 


3. 
S -> '(' L ')' | 'a'

L -> S M 

M -> ',' S M|


4. 
S -> '1' S | '0' T | 

T -> '1' T | '0' S


5. 
A -> 'a' B E

E -> 'd' E | 

B -> 'b'

C -> 'g'


Finally, the library will confirm whether or not the string is valid depending on the predefined structures. If an entered terminal does not belong to the grammar, the program will notify about the error.

Explanatory note: the strings must be entered separated by spaces, this is an example of a valid string for grammar 1:

digit * ( digit ) * digit + digit + ( digit )

as you can see, between token and token there must be a space. Also within the definition of grammars, epsilon is defined as an empty space

# google colab link with the code:

https://colab.research.google.com/drive/1xAVtBapsQ7pZk3nYR6ugJ18gAtIDMk4X?usp=sharing

