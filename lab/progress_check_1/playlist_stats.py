CLASS_CODE = "CS111_W26_STATS_FOR_FUN"
def total_time(len_seconds):
    hours = len_seconds // 3600
    remainder = len_seconds % 3600
    minute = remainder // 60
    second = remainder % 60
    return f'{hours}:{minute:02}:{second:02}'

if __name__ == "__main__":
    user_input = input('Enter the filename of the playlist in .csv format:\n')
    openfile = open(user_input, 'r')

    all_artists = []
    all_songs = []
    times_played = 0
    time = 0
    for line in openfile:
        print(line)
        split_line = line.split(',')
        fifth_element = split_line[5]
        all_songs.append(split_line[0])
        all_artists.append(split_line[1])
        if int(fifth_element) > times_played:
            fav_song = split_line[0]
            times_played = int(fifth_element)
        time_element = split_line[3]
        time_element = time_element.split(':')
        minutes , seconds = time_element
        time += (int(minutes) * 60) + int(seconds)




    print(f'The playlist has {len(all_songs)} songs.')
    print(f'The first song is {all_songs[0]} by {all_artists[0]}.')
    print(f'The last song is {all_songs[-1]} by {all_artists[-1]}.')
    print(f'{fav_song} was played the most times at {times_played} plays.')
    print(f'The playlist is {total_time(time)}')


