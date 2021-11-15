"""
Update this module docstring with your own details
Name:
Date started:
"""


def display_menu():
    """
    display menu
    """
    print('Menu:')
    print('L - List all albums')
    print('A - Add new album')
    print('M - Mark an album as completed')
    print('Q - Quit')


def load(filename):
    """
    load a CSV (Comma Separated Values) file of albums (just once at the very start); a
    sample CSV file is provided for you and you must use this format [5] (note: you're not
    expected to use the csv module, but you're welcome to)
    :param filename:  file name
    :return: data in the file
    """
    data = []
    with open(filename) as f:
        line = f.readline().strip()
        while (line):
            item = line.split(',')
            data.append(item)
            line = f.readline().strip()
    return data


def display_data(data):
    """
    when the user chooses list: display a neatly formatted (lined up) list of all the albums
    with their details and the number of albums you need to listen to [4]. Required albums
    have a * next to them. Note that the lining up is based on the longest title and artist [6]
    Users can choose to display the list of albums , which will be sorted by artist, then by title.
    :param data: data in the file
    """
    count_unlisten = 0
    for i in range(len(data)):
        item = data[i]
        if (item[3] == 'r'):
            count_unlisten += 1
            print('*{}. {:<30}by {:14} ({})'.format(i + 1, item[0], item[1], item[2]))
        else:
            print(' {}. {:<30}by {:14} ({})'.format(i + 1, item[0], item[1], item[2]))
    if count_unlisten == 0:
        print('No albums left to listen to. Why not add a new album?')
    else:
        print('You need to listen to {} albums.'.format(count_unlisten))


def add_data(data):
    """
    prompt for the album’s title, artist and year, error-checking each of these [3], then add the album to the list in memory (not to the
    file); new albums are always required
    :param data: origin data
    :return: new data
    """
    title = ''
    artist = ''
    year = ''
    # input Title
    while (True):
        title = input('Title: ')
        if (title == ''):
            print('Input can not be blank')
        else:
            break
    # input Artist
    while (True):
        artist = input('Artist: ')
        if (artist == ''):
            print('Input can not be blank')
        else:
            break
    # input Year
    while (True):
        try:
            year = int(input('Year: '))
        except Exception as e:
            print('Invalid input; enter a valid number')
            continue
        if (year <= 0):
            print('Number must be > 0')
            continue
        else:
            break
    # add data
    data.append([title, artist, str(year), 'r'])
    print('{} by {} ({}) added to Album Tracker'.format(title, artist, year))
    return data


def mark(data):
    """
    display the list of all albums (same as for the
    list option), then allow the user to choose one album (error-checked), then change that album to completed
    o if there are no required albums, then "No required albums" should be displayed
    :param data: origin data
    :return: new data
    """
    while (True):
        try:
            mark_index = int(input('>>> '))
        except Exception as e:
            print('Invalid input; enter a valid number')
            continue
        if (mark_index <= 0):
            print('Number must be > 0')
        elif (data[mark_index - 1][3] == 'c'):
            print('You have already listened to {}'.format(data[mark_index - 1][0]))
            break
        elif (data[mark_index - 1][3] == 'r'):
            data[mark_index - 1][3] = 'c'
            print('You listened to {} by {}'.format(data[mark_index - 1][0], data[mark_index - 1][1]))
            break
    return data


def save_file(data):
    """
    when the user chooses quit: save the albums to the CSV file (note that this should be
    the only time that the file is saved)
    :param data: new data
    """
    with open('albums.csv', 'w') as f:
        for item in data:
            f.write(','.join(item) + '\n')


def main():
    # • display a welcome message with your name
    print("Album Tracker 1.0 - by <Ou Liu>")
    # load a CSV (Comma Separated Values) file of albums (just once at the very start); a
    data = load('albums.csv')
    data = sorted(data, key=lambda x: (x[1], x[0]))
    print('{} albums loaded'.format(len(data)))
    while (True):
        # display a menu for the user to choose from [2, 3]
        display_menu()
        # error-check user inputs (see sample output for example checks and outputs) [4]
        validChoices = ['l', 'a', 'm', 'q']
        choice = input('>>> ')
        # convert to lower case
        choice = choice.lower()
        # input menu choice
        if (choice not in validChoices):
            print('Invalid menu choice')
            # list the data
        elif (choice == 'l'):
            display_data(data)
            # add album
        elif (choice == 'a'):
            data = add_data(data)
            data = sorted(data, key=lambda x: (x[1], x[0]))
            # mark album as listened
        elif (choice == 'm'):
            # count un listen albums
            countUnlisten = 0
            for i in range(len(data)):
                item = data[i]
                if (item[3] == 'r'):
                    countUnlisten += 1
            # No required albums
            if (countUnlisten == 0):
                print('No required albums')
            else:
                display_data(data)
                data = mark(data)
        elif (choice == 'q'):
            # save the new albums to albums.csv
            save_file(data)
            print('{} albums saved to albums.csv'.format(len(data)))
            break


main()
