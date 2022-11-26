import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True: 
        city = input("Enter a city: ")
        if city.lower() not in ('chicago', 'new york City', 'washington'): 
            print("Invalid City, Please try Chicago, New York City, Washington")
            continue
        else: 
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month: ")
        if month.lower() not in ('january', 'february', 'march', 'april','may','june','all'):
            print("Invalid Month, Please try months January through June or view all data for available months")
            continue
        else: 
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input("Enter day of week: ")
        if day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'):
            print("Invalid Day, Please try days Monday through Sunday or view all data for available days") 
            continue
        else: 
            break


    print('-'*40)
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
    new_var = df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january','february','march','april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all': 
        df = df[df['day_of_week'] == day.title()]
    new_var

    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Popular Month: ', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Popular Day: ',common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Day: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips taken...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('Most Commonly used start station: ', Start_Station)

    # display most commonly used end station
    End_Station = new_func(df)
    print('Most Commonly used End station: ', End_Station)


    # display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('Most common trips for start and end stations: ', Start_Station, "&", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def new_func(df):
    End_Station = df['End Station'].mode()[0]
    return End_Station


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time: ', total_travel_time/86400, "Days")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time/60, "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)


    # Display counts of gender
    try: 
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types) 
    except KeyError: 
        print("\nGender Types:\nData unavailable for this month.")

    # Display earliest, most recent, and most common year of birth
    try: 
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError: 
        print("\nEarliest Year:\nNo data available for this month.")
    try: 
        recent_birth_year = df['Birth Year'].max()
        print('\nMost Recent Year:', recent_birth_year)
    except KeyError: 
        print("\nMost Recent Year:\nNo data available for this month.")
    try: 
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Birth Year:', common_birth_year)
    except KeyError: 
        print("\nMost Common Birth Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def individual_trip_date():
    while True:
        
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        
        if view_display != 'yes':
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
