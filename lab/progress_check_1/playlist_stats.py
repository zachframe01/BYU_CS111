CLASS_CODE = "CS111_W26_STATS_FOR_FUN"

def hours_minutes_seconds(x):
    hours = x // 3600
    remaining = x % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return (f'{hours}:{minutes:02}:{seconds:02}')

if __name__ == "__main__":
    user_playlist = input("Enter the filename of the playlist in .csv format: \n")

    open_file = open(user_playlist, "r")
    count = 0
    times_played = 0
    total_time = 0
    all_songs = []
    all_singers = []
    for line in open_file:
        split_line = line.split(",")
        all_songs.append(split_line[0])
        all_singers.append(split_line[1])
        song_length = split_line[3]
        minutes , seconds = song_length.split(":")
        total_time += (int(minutes) * 60) + (int(seconds))

        if int(split_line[5]) > times_played:
            times_played = int(split_line[5])
            fav_song = split_line[0]

        count += 1
    
    print(f'The playlist has {count} songs. ')
    print(f'The first song is {all_songs[0]} by {all_singers[0]}. ')
    print(f'The last song is {all_songs[-1]} by {all_singers[-1]}.')
    print(f'{fav_song} was played the most times at {times_played} plays.')
    print(f'the playlist is {hours_minutes_seconds(total_time)} long.')
    
    open_file.close()