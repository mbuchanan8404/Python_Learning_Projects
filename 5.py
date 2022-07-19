#######################################
# Matthew Ryan Buchanan
# BMI calculator
#######################################

# This program will take a list of people with their height in meters and weight in kilograms
# and return a score based on a BMI calculation. Possible scores are: Underweight, Normal weight, Overweight, and Obese


# Function to get input for the list of people and their stats
def get_stats():
    people = []
    number_of_people = int(input("Please enter the number of people to score: "))
    for person in range(0, number_of_people):
        new_person = []
        new_person.append(float(input("Please enter the person's weight in kilograms: ")))
        new_person.append(float(input("Please enter the person's height in meters: ")))
        people.append(new_person)
    calculate_bmi(people)


# Function to calculate the BMI of each person
def calculate_bmi(lst_of_stats):
    lst_of_bmi = [weight / (height * height) for [weight,height] in lst_of_stats] # perform the bmi calculation: bmi = weight/height^2
    output_scores(lst_of_bmi)
    

# Function to output the scores of each person
def output_scores(bmi_lst):
    scores = []
    print("answer:")
    for bmi in bmi_lst:
        if bmi < 18.5:
            scores.append("under")
        elif bmi >= 18.5 and bmi < 25.0:
            scores.append("normal")
        elif bmi >= 25.0 and bmi < 30.0:
            scores.append("over")
        else:
            scores.append("obese")
    final_output = ""
    for score in scores:
        final_output += score + " " 
    print(final_output)


get_stats() # Start this depression generator