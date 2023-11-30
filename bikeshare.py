import time
import pandas as pd


# Reviewer note: please make sure that you adapt the cities path in the below dictionary
# so that the code can grab it from correct path... otherwise place the CSV's inside a subfolder 'cities'...
# I wanted to have my py-file and my data files in a separated "environment" (= subfolder 'cities' for the CSV's)!!!

CITY_DATA = {'chicago': './cities/chicago.csv',
             'new york city': './cities/new_york_city.csv',
             'washington': './cities/washington.csv'}
valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = list(CITY_DATA.keys())
    while True:
        city = str(input('Please type any city you are interested in: ')).lower()
        if city not in cities:
            print(f'This wasn\'t any valid city selection. \nPlease select one out of the following list: \n'
                  f'   {cities}')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Please type any month you are interested in or type >all< to get full summary. \n' +
                          'Note that there are only month valid between >January< and >June<: ')).lower()
        if month not in valid_months:
            print(f'This wasn\'t any valid month selection. \nPlease select one out of the following list: \n' +
                  f'   {valid_months}')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Please type any day you are interested in or type >all< to get full summary. \n' +
                        'Note that there are all days valid between >Monday< and >Sunday<: ')).lower()
        if day not in valid_days:
            print(f'This wasn\'t any valid day selection. \nPlease select one out of the following list: \n' +
                  f'   {valid_days}')
        else:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load the data into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new columns for month & day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # exception handling for all@months, filtering month
    if month != 'all':
        sel_month = valid_months.index(month)
        df = df[df['month'] == sel_month]

    # exception handling for all@days, filtering day
    if day != 'all':
        sel_day = valid_days.index(day) - 1
        df = df[df['day_of_week'] == sel_day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month = valid_months[most_common_month].title()
    print(f"The most common month is {most_common_month}")

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    most_common_day = (valid_days[most_common_day + 1]).title()
    print(f"The most common day of the week is {most_common_day}.")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"The most common start hour is {most_common_hour} o\'clock.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is {start_station}.")

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is {end_station}.")

    # display most frequent combination of start station and end station trip
    most_frequent_combi = df['Start Station'].map(str) + ' -> ' + df['End Station']
    most_frequent_route = most_frequent_combi.mode()[0]
    print(f"The most frequent combination is: {most_frequent_route}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    minutes, seconds = divmod(total_duration, 60)
    hours, minutes = divmod(minutes, 60)
    print(f"The total travel time is: {hours} hour(s), {minutes} minute(s) and {seconds} second(s)")

    # reset time values
    hours, minutes, seconds = None, None, None

    # display mean travel time
    mean_time = round(df['Trip Duration'].mean())
    minutes, seconds = divmod(mean_time, 60)
    hours, minutes = divmod(minutes, 60)
    print(f"The mean travel time is: {hours} hour(s), {minutes} minute(s) and {seconds} second(s)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types, "\n")

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
    except KeyError:
        print(f"{KeyError} -> Key 'Gender' wasn\'t found in current selection!")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    else:
        print(user_gender, "\n")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
    except KeyError:
        print(f"{KeyError} -> Key 'Birth Year' wasn\'t found in current selection!")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    else:
        print(f"The earliest year of birth is: {earliest_year_of_birth},\n" +
              f"the most recent year of birth is: {most_recent_year_of_birth},\n" +
              f"and the most common year of birth is: {most_common_year_of_birth}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Displays some rows of raw data """
    start_loc = 0
    view_data = ''

    while True:
        if start_loc == 0:
            view_data = input("\nWould you like to view 5 rows of individual trip data? Enter 'yes' or 'no'\n").lower()
        else:
            view_data = input("Do you wish to continue and show 5 more rows ('yes' or 'no')?: ").lower()

        if view_data == 'yes':
            print(f"Showing row {start_loc + 1} to {start_loc + 5}")
            print(df.iloc[start_loc:(start_loc + 5)])
            start_loc += 5
        else:
            break

    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
