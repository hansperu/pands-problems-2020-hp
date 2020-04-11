mysentence = (input("Enter a string : "))
# Input (Entrada)
str = "The quick brown fox jumps over the lazy dog." 
# initial string (cadena inicial)
reversed = "".join(reversed(str)) 
#.join() method merges all of the characters (conbina todos los caracteres)
print("Every second letter of your reversed string:", reversed[0:43:2]) 
# print the reversed string (imprimir la cadena invertida)
