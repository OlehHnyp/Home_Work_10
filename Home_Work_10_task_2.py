def day_of_week(day):
    days = {1: 'Monday',
            2: 'Tuesday',
            3: 'Thirsday',
            4: 'Wednesday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'}
    try:
        if day == str(day):
            day = int(day)
            raise IndexError
        
        if 0<day<8:
            return days.get(day)
        else:
            raise IndexError

    except ValueError:
        return "You did not enter a number! Please try again."
    except IndexError:
        return "There is no such day of the week! Please try again."