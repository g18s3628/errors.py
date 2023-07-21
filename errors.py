# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#print "Welcome to the error program"
print("Welcome to the error program") #Syntax error: Missing parentheses  
    #print "\n"
print("\n") #Syntax error: Missing parentheses and incorrect indentation

    #Variables declaring the user's age, casting the str to an int, and printing the result
    #age_Str == "24 years old" 
age_Str = "24"#Syntax error: Incorrect indentation and double equal sign instead of one to assign variable
    #age = int(age_Str) 
age = int(age_Str) 
    #print("I'm" + age + "years old.")
print("I'm " + str(age) + " years old.") 
#Logical error: age_Str contains alphabets instead of just numerical values 
#Runtime error: Putting together an integer and a string but did not convert the integer to a string 

    # Variables declaring additional years and printing the total years of age
    #years_from_now = "3"
years_from_now = 3 #Logical error: Assiging as string instead of an integer
    #total_years = age + years_from_now
total_years = age + years_from_now #Syntax error:Unexpected indentation 
#print "The total number of years:" + "answer_years"
print("The total number of years:", str(total_years)) #Logical error: The variable answer_years is not defined 

# Variable to calculate the total amount of months from the total amount of years and printing the result
#total_months = total * 12
total_months = (total_years * 12) + 6 #Logical error: Using total instead of total_years and not adding the 6 months to get the 330 months 
#print "In 3 years and 6 months, I'll be " + total_months + " months old"
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
#Syntax error: Missing parentheses
#Runtime error: Putting together an integer and a string but did not convert the integer to a string 
#HINT, 330 months is the correct answer
