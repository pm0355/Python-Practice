#/**********************************************************************/ 
#/* CSC 280 - 3rd proj
#/* */ 
#/* modifier: Paul Mattioli
#/* */ 
#/* filename:max_min_tri.py 
#/* modified from: my laptop 
#/* date last modified: 10/6/2013 
#/* */ 
#/* action:takes 3 inputs and  calculates and outputs max and min values 
#/* */ 
#/* input: raw input numbers from user
#/* */ 
#/* output: outputs max and min values
#/* */ 
#/* */ 
#/**********************************************************************/ 

''' here i set variables equal to a raw input and prompts for 3 numbers '''

a = float(raw_input(" Enter the first number: "))
b = float(raw_input(" Enter the second number: "))
c = float(raw_input(" Enter the third number: "))


if a > b:
    if a > c:
        print str(a) + " is the max"
        if b > c:
            print str(c) + " is the min"   
        else:
            print str(b) + " is the min"
    else:
        print str(c) + " is the max"
        print str(b) + " is the min"
           
else:
    if b > c:
        print str(b) + " is the max"
        if a > c:
            print str(c) + " is the min"
    else:
        print str(c) + " is the max"
        print str(a) + " is the min"
    
