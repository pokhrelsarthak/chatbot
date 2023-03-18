# Define the Harris-Benedict equation for men and women
def calculate_bmr(height, weight, gender, age, activity_level):
    # Define the activity level factors
    activity_levels = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    bmr = 0
    if gender == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender == 'female':
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    daily_calorie_needs = bmr * activity_levels[activity_level]
    return daily_calorie_needs

    