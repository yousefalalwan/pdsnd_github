import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    """
    print('Hello! Let\'s explore some US bikeshare data!')

    """ We are going to ask the user to enter a name of city through an interactive code"""
    while True:
        city = input('Choose one of those cities chicago, new york city, washington: ').lower()
        if city in CITY_DATA.keys():
            print('The chosen city is: ', city)
            break
        else:
            print('Opps, you entered a wrong city, please enter either new york city, chicago or washington')
            continue
    """ We are going to ask the user to enter a month or all to display all of the data through an interactive code"""
    while True:
        month = input('Enter a month in such format all, januray, ..., june: ').lower()
        months = ['januray', 'february', 'march', 'april', 'may', 'june']
        if month in months:
            print('let us get the data for: ', month.title())
            break
        elif month == 'all':
            print('display all of the months data')
            break
        else:
            print('Ops, you entered a wrong month, please enter the right month')
            continue


    """ We are going to ask the user to enter a day or all to display the whole month through an interactive code"""
    while True:
        day = input('enter a day in such format all, monday, tuesday, ... sunday: ').lower()
        days = ['monday','tuesday', 'wednesday','thursday','friday','saturday','sunday' ]
        if day == 'all':
            print('Display all of the days data')
            break
        elif day in days:
            print('display the data of: ', day.title())
            break
        else:
            print('Please enter a correct day')
            continue


    print('-'*40)
    """ A call for the function to return the entered values from the user"""
    return city, month, day


def load_data(city, month, day):
    """ A script that is using pandas's functions to download the data from the given files, and to display the data through data frame in a similar way as excel tables. For the first line of code we are reading the given files, and the second line we are arraning them in a table. [city] here is corresponding to the entered city from the user.
    """
    """ df the dataframe that returns the data from the downloaded files
        to illustrate the data through the given code.
    """
    file = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(file)
    """ We are using pd.to_datetime function to create new columns for month, day and hour. """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    """filtering by month:"""
    if month != 'all':
        """using the index of months list to get the corresponding int"""
        months = ['januray', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        """filtering by monthing through new dataframe"""
        df = df[df['month'] == month]
    if day != 'all':
        """filter by day of the week to create the new dataframe"""
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):


    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """
        Here we are utilizing what we learend through the course and Pandas functions to
        display the most frequent month, day and hour that the bikes are being rented and used by
        the mode() function.
    """
    most_month = df['month'].mode()[0]
    print()
    print('The most common month is: ', most_month)
    print()

    """ Note using print() as a space to make it more readable"""


    most_day = df['day'].mode()[0]
    print('The most common day of week: ', most_day)
    print()


    most_hr = df['hour'].mode()[0]
    print('The most common hour starting hour: ', most_hr )
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """
    This is a code that is displaying the most frequent start and end station
    based on the city that was entered from the user. We are utilizing similar
    functions that are were utilized in the previous function.

    """



    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print()

    most_start_station = df['Start Station'].mode()

    print('Them most commonly used start station is: ', most_start_station  )


    most_end_station = df['End Station'].mode()
    print('The most commonly used end station is: ', most_end_station  )
    print()


    """
    Here is a small trick that allows us to display
    the most frequent combination between two different
    columns that are start and end station at this particular
    example.
    """
    most_frequent_combination = df.groupby([ 'Start Station', 'End Station']).size().sort_values(ascending=False).index[0]
    most_frequent_start_station = most_frequent_combination[0]
    most_frequent_end_station = most_frequent_combination[1]
    print(f'The most frequent combination of start and end station is: {most_frequent_start_station}, {most_frequent_end_station },')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """
    Here is a code that is utilizing Pandas fucntions to display the
    total time for all trip durations and their average.
    """
    """ We are using sum function to calucate the total travel time"""
    total_travel_time = df['Trip Duration'].sum()
    print(f'The total travel duration is: {total_travel_time:.2f}' )


    """ we are using the mean function to calculate the average traveling time """
    avg_travel_time = df['Trip Duration'].mean()
    print(f'The average travel duration is: {avg_travel_time:.2f}' )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """
    Here is a code that displays different querys, the first line of the code
    will count for us how many of the users are subcribers, the second line
    will specify the gender, note this is only possbile for Chicago and NYC,
    and that is why we seized the try and except method to overcome an error if
    the user selected Washington, since Washington file does not have any data
    about the gender or the birth year of the bikers. We dispalyed through
    Pandas functions, how many males and females rented a bike,
    what is oldest and youngest of them and the most common birth year.
    """

    """ Counting the number of the subcribers """
    subscribers = df[df['User Type'] == 'Subscriber']['User Type'].count()
    print()
    print('This is the count of the subscribers : ', subscribers)

    """ Counting the number of the customers """
    customers = df[df['User Type'] == 'Customer']['User Type'].count()
    print()
    print('This is the count of the customers : ', customers )

    """
        Seizing the try and except method to overcome the keyerror that occurs due to
        washington file, since it does not have any data related to the Gender
    """
    try:
        """ Display counts of males """
        Males = df[df['Gender'] == 'Male']['User Type'].count()
        print('The number of males : ', Males)

        """ Display counts of females """
        Females = df[df['Gender'] == 'Female']['User Type'].count()
        print()
        print('The number of Females : ', df[df['Gender'] == 'Female']['User Type'].count())
        """ Display counts of both genders """
        both_genders = df['Gender'].count()
        print()
        print('The count of both genders is: ', both_genders)

        """
        Display earliest, most recent, and most common year of birth
        """
        """ We are asking the code to call on the youngest biker """
        youngest_biker = df['Birth Year'].min()
        print()
        print('The earliet year of birth is: ', youngest_biker)
        """ We are asking the code to call on the oldest biker """
        oldest_biker = df['Birth Year'].max()
        print()
        print('The most recent year of birth is: ', oldest_biker)

        """ We are asking the code to call on the most common age """
        most_common_age = df['Birth Year'].mode()[0]
        print()
        print('The most common year of birth is: ', most_common_age)
        print()
    except KeyError:

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        return df
def raw_input(df):
    """
    Here we created a function that will display the raw data if the user
    wished so, we used while loop and counter to display further raw data
    if the user wished too.
    """
    """ we made data equals to zero to define it to the loop """
    data = 0
    """"
    A while loop to allow the user to iterate through the datframe and to be able to
    ask the code to pull five rows of raw input for the user, and another five rows
    till the user is statsified. Then we used break to stop the loop otherwise it will
    keep running.
    """
    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df.iloc[data:data+5, :])
            data += 5
        else:
            break
    return df


def main():

    """"
    while loop to allow the user to be to check the data for different
    cities and dates if the user desired to do so.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break





if __name__ == "__main__":
	main()


"""
    Resources:

    https://stackoverflow.com
    https://www.geeksforgeeks.org
    https://pandas.pydata.org
    https://www.youtube.com/@CSDojo
    https://www.youtube.com/@GiraffeAcademy
    https://www.youtube.com/@Telusko
    https://www.w3schools.com
    https://realpython.com
    https://bobbyhadz.com
    Notes from our instructors

"""
