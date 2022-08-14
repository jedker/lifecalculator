#User input for DOB
age = input("Wpisz swoją datę urodzenia w formacie dd.mm.yyyy (pamiętaj - kropki, nie przecinki)\n")
#User input for current date
date = input("Wpisz obecną datę w formacie dd.mm.yyyy\n")
#converting DOB and current date to integer
birth_year = int(age[6:10])
birth_month = int(age[3:5])
birth_day = int(age[0:2])

current_day = int(date[0:2])
current_month = int(date[3:5])
current_year = int(date[6:10])

#User input for desired years
desired_age_years = input("Wpisz ile lat chciałbyś żyć w formacie yy\n")
#count desired age into days, months and years
desired_age_months = float(desired_age_years) * 12
desired_age_days = float(desired_age_years) * 365.25
#extract value for year in months
number_of_days_in_month = 365.25 / 12
number_of_months_in_year = 365.25 / number_of_days_in_month
number_of_days_in_year = 365.25
#functions that adds or subtracts months to current age 

def monthCount():
  month_count = 0
  if birth_month >= current_month:
    month_count -= (birth_month - current_month) * number_of_days_in_month
    return(month_count)
  if birth_month < current_month:
    month_count += (current_month - birth_month) * number_of_days_in_month
    return(month_count)
def daysCount():
  days_count = 0
  if birth_day >= current_day:
    days_count -= (birth_day - current_day) 
    return(days_count)
  if birth_day < current_day:
    days_count += (current_day - birth_day) 
    return(days_count)
#functions used to determine current age in days
current_age_days = (current_year - birth_year) * number_of_days_in_year + monthCount() +daysCount()
#days counted for weeks
current_age_weeks = current_age_days / 7
desired_age_weeks = desired_age_days / 7
weeks_left = desired_age_weeks - current_age_weeks
#program output to user: weeks of life left and lived
print(f"Jeśli będziesz żył {desired_age_years} lat, przeżyłeś już:\n{round(current_age_weeks, 1)} tygodni. \nZostało Ci: \n{round(weeks_left, 1 )} tygodni.")
#function for percentage
def percentage(current_age_weeks, desired_age_weeks):
  Percentage = 100 * float(current_age_weeks)/float(desired_age_weeks)
  return str(f"{round(Percentage, 1)}%") 
#program output to user: % of life
print("Przeżyłeś już ", percentage(current_age_weeks, desired_age_weeks) + " życia.\nNie spierdol reszty.")










