def days_since_birthday(birthday):
    try:
        birth_year = int(birthday.split("-")[2])
        current_year = 2024
        whole_years_passed = (current_year - 1) - (birth_year + 1) + 1
        days_passed = whole_years_passed * 365

        print("Approximately", days_passed,
              "days have passed since your birthday, excluding the days in your birth year and the current year.")
    except ValueError:
        print("Please enter your birthday in 'DD-MM-YYYY' format.")

birthday = input("Enter your birthday in 'DD-MM-YYYY' format: ")
days_since_birthday(birthday)
