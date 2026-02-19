CLASS_CODE = "CS111_W26_STATS_FOR_FUN"

def hours_minutes_seconds(x):
    hours = x // 3600
    remaining = x % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return (f'{hours}:{minutes:02}:{seconds:02}')

if __name__ == "__main__":
    user_playlist = input("please type in your file: \n")

    open_file = open(user_playlist , "r")
    
    for line in open_file:
        print(line)
