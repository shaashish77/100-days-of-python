age = int(input("What is your current age?\n"))

age_as_int = int(age)

years_rem = 90-age_as_int

days_rem = years_rem * 365

weeks_rem = years_rem * 52

months_rem = years_rem * 12

message= f"You have {days_rem} days, {weeks_rem} weeks, {months_rem} months, {years_rem} years remaining"

print(message)
