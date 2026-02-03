CLASS_CODE = "CS111_W26_STATS_FOR_FUN"


if __name__ == "__main__":
    playlist1 = open("playlist1.csv", "r")
    playlist2 = open("playlist2.csv", "r")
    playlist3 = open("playlist3.csv", "r")

    
    user_playlist = input("input your playlist file name: ")
    user_chosen = 0 
    if user_playlist == "playlist1.csv" or "playlist1":
        user_chosen = 1
    elif user_playlist == "playlist2.csv" or "playlist2":
        user_chosen = 2
    elif user_playlist == "playlist3.csv" or "playlist3":
        user_chosen = 3

    
    if  user_chosen == 1:
        playlist1 = open("playlist1.csv", "r")
        chosen = playlist1
    elif user_chosen == 2:
        playlist2 = open("playlist2.csv", "r")
        chosen = playlist2
    elif user_chosen == 3:
        playlist3 = open("playlist3.csv", "r")
        chosen = playlist3
    else:
        print("something is wrong")

    
    count = 0
    all_songs = []
    all_singers = []
    popular_song = 0
    total_times_played = 0
    total_time = 0
    for line in chosen:
        clean_line = line.split(',')
        all_songs.append(clean_line[0])
        all_singers.append(clean_line[1])
        times_played = int(clean_line[5])
        if popular_song < times_played:
            total_times_played = int(clean_line[5])
            fav_song = clean_line[0]
            popular_song = total_times_played

        count += 1


    print(f'the playlist has {count} songs')
    print(f'The first song is {all_songs[0]} by {all_singers[0]}.')
    print(f'The last song is {all_songs[-1]} by {all_singers[-1]}.')
    print(f'{fav_song} was played the most times at {total_times_played} plays.')

    playlist1.close()
    playlist2.close()
    playlist3.close()