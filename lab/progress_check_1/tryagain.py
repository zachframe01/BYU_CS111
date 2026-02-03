def total_playlist_time(x):
    hours = x // 3600
    remaining = x % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return f'{hours}:{minutes:02}:{seconds:02}'



if __name__ == "__main__":
    file = input("Enter the filename of the playlist in .csv format: ")
    open_file = open(file, "r")


    count = 0 
    singers = []
    songs = []
    times_played = 0
    total_time = 0
    for line in open_file:
        split_line = line.split(",")
        songs.append(split_line[0])
        singers.append(split_line[1])
        if int(split_line[5]) > times_played:
            times_played = int(split_line[5])
            fav_song = split_line[0]
        minutes , seconds = split_line[3].split(':')
        total_time += ((int(minutes) * 60) + int(seconds) )


        count += 1

    print(f"The playlist has {count} songs.")
    print(f"The first song is {songs[0]} by {singers[0]}.")
    print(f"The last song is {songs[-1]} by {singers[-1]}.")
    print(f"{fav_song} was played the most times at {times_played} plays.")
    print(f"The playlist is {total_playlist_time(total_time)} long.")
    
    open_file.close