import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many people of each race?
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(),
        1
    )

    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # People with advanced education
    advanced_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    # Percentage of people with advanced education
    # who make more than 50K
    higher_education_rich = round(
        (
            df.loc[advanced_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Percentage of people without advanced education
    # who make more than 50K
    lower_education_rich = round(
        (
            df.loc[~advanced_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Minimum number of hours a person works per week
    min_work_hours = df["hours-per-week"].min()

    # People who work the minimum number of hours
    min_hours_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    # Percentage of people who work minimum hours
    # and earn more than 50K
    rich_percentage = round(
        (
            min_hours_workers["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Country with the highest percentage of people
    # who earn more than 50K
    country_percentage = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(),
        1
    )

    # Most popular occupation for people in India
    # who earn more than 50K
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)

        print("Average age of men:")
        print(average_age_men)

        print(
            "Percentage of people who have a Bachelor's degree:"
        )
        print(percentage_bachelors)

        print(
            "Percentage of people with advanced education "
            "that earn >50K:"
        )
        print(higher_education_rich)

        print(
            "Percentage of people without advanced education "
            "that earn >50K:"
        )
        print(lower_education_rich)

        print("Minimum number of hours a person works per week:")
        print(min_work_hours)

        print(
            "Percentage of people who earn >50K "
            "among those who work minimum hours:"
        )
        print(rich_percentage)

        print(
            "Country with the highest percentage of people "
            "that earn >50K:"
        )
        print(highest_earning_country)

        print(
            "Percentage of people who earn >50K in that country:"
        )
        print(highest_earning_country_percentage)

        print(
            "Most popular occupation for people in India "
            "who earn >50K:"
        )
        print(top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }