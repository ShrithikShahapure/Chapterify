
#function to convert time
def convert_time(decimal_time):
    hours = int(decimal_time // 3600)
    minutes = int((decimal_time % 3600) // 60)
    seconds = int(decimal_time % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
