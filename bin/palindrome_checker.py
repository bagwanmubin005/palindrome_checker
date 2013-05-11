#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import re

def main():
        try:
                # If called without arguments, get string from standard input.
                if len(sys.argv) == 1:
                        # Read string from standard input
                        string = str(raw_input("Enter string to check: "))
                # Otherwise, make sure the program is called with exactly one argument.
                # sys.argv is the number of args + 1 because
                # the program's name is in sys.argv[0]
                elif len(sys.argv) != 2:
                        print "invalid arguments (%d), usage: %s [string]" % (len(sys.argv), sys.argv[0])
                        return 1


                # Compile regex matching digits, punctuation characters and blanks.
                special_characters = re.compile( '[,;.:_!?0-9 -]+')
                #print your entered string this may contain many unwanted characters
                print "your Entered String is : "+string
                # Remove special characters from string and set our string varialble
                # to the resulting string returned.
                #remove numbers, !, [,],:,;+- from input
                string = special_characters.sub( '', string)
                print "String after removing special numbers,punctuation marks,+,! : "+string

                # Because the lower() method does not support unicode,
                # remove any non supported characters before comparing.
                #this is the regular expression to take pattern containing a-z & A-Z
                invalid_characters = re.compile( '[^a-zA-Z]')
                #print invalid_characters       
                # Replace invalid characters with a dot character.
                string = invalid_characters.sub( '.', string)
                #print "String after removing invalid characters (replaced with .) : "+string
                # Convert all upper case characters to lower case.
                string = string.lower()

                # Reverse string.
                reversed_string = string[::-1]

                # Check if string is equal to the reversed string.
                if reversed_string == string:
                        # The string is a palidrome.
                        print "yes"
                else:
                        # The string is not a palidrome.
                        print "no"
                return 0
        except:
                print "unknown error, usage: %s [string]" % sys.argv[0]
                return 2
-- INSERT --                                                                                                              34,7-17       Top
