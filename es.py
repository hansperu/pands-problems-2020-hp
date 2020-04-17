# program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

import sys
import os

#Source1 https://stackabuse.com/command-line-arguments-in-python/
#Sourse2 https://riptutorial.com/es/python/example/6530/usando-argumentos-de-linea-de-comando-con-argv
#Source3 https://stackoverflow.com/questions/23232248/python-3-4-counting-occurrences-in-a-txt-file
#Sourse4 https://micro.recursospython.com/recursos/como-obtener-los-argumentos-de-la-linea-de-comandos.html
def main():
    
    current_directory = os.getcwd()
    current_file = current_directory + "\\" + str(sys.argv[1]) 
    print("\nNow analysing " + current_file + "\nand counting the number of e(s)")

    file  = open(current_file, 'r').read() 
    analyse  = "e"
    count = file.count(analyse)
    print("\nNumber of e found: ", count)

    main()