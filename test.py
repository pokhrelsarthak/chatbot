# Define the Harris-Benedict equation for men
def calculate_bmr(gender, weight, height, age):
    if gender == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height*100) - (5.7 * age)
        
        # 10W + 6.25H - 5A + 5

        # bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        
    return bmr

# Define the activity level factors
activity_levels = {
    'sedentary': 1.2,
    'lightly active': 1.375,
    'moderately active': 1.55,
    'very active': 1.725,
    'extra active': 1.9
}

# Get user input
gender = 'male'
weight = 70   # kg
height = 1.75   # meters
age = 21   # years
activity_level = 'moderately active'

# Calculate BMR and daily calorie needs
bmr = calculate_bmr(gender, weight, height, age)
daily_calorie_needs = bmr * activity_levels[activity_level]

# Print the result
print("Your daily calorie needs are: {:.2f} calories".format(daily_calorie_needs))
