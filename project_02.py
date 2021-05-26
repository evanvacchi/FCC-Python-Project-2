def add_time(start, duration, day = ''):
    start_hours = list(range(1,13))
    #print(start_hours)
    start_minutes = list(range(0,60))
    #print(start_minutes_2)
    start_ending = [' AM', ' PM']
    #print(start_ending)
    # -------------------------------------------------------------
    #need to add not negative conditional, 00-09  for hours too?
    duration_hours = 69
    hours_whole_number = isinstance(69, int) #if true (whole number) use it for hours
    #print(hours, duration_hours)
    duration_minutes = list(range(0,60))

    #start = '6:30 PM' #placeholder
    #start = 'start_hours' + ':' + 'start_minutes' + 'start_ending'
    #duration = '205:12'
    #duration = 'duration_hours' + ':' + 'duration_minutes'
    ampm = 'AM/PM'

    if ':' == start[1]:
        starting_hours = int(start[0])
        #print('Starting hour', starting_hours)
        if '0' == start[2]:
            starting_minutes = int(start[3])
            #print('Starting minutes', starting_minutes)
        else:
            starting_minutes = int(start[2] + start[3])
            #print('Starting minutes', starting_minutes)

    elif ':' == start[2]:
        starting_hours = int(start[0] + start[1])
        #print('Starting hour', starting_hours)
        if '0' == start[3]:
            starting_minutes = int(start[4])
            #print('Starting minutes', starting_minutes)
        else:
            starting_minutes = int(start[3] + start[4])
            #print('Starting minutes', starting_minutes)

    separator = duration.index(':')
    #print('colon', separator, duration[2], duration[separator])
    if ':' == duration[separator]:
        duration_hours = int(duration[:separator])
        #print('Duration hours', duration_hours)
        if '0' == duration[separator+1]:
            duration_minutes = int(duration[separator+2])
            #print('Duration minutes', duration_minutes)
        else:
            duration_minutes = int(duration[separator+1:])
            #print('Duration minutes', duration_minutes)

    counter = 0
    new_minutes = starting_minutes + duration_minutes
    new_hours = starting_hours + duration_hours
    if new_minutes > 59:
        new_hours = new_hours + int(new_minutes/60) #extra minutes to hours
        new_minutes = new_minutes % 60 #leftover minutes
    if new_hours >= 12:
        counter = int(new_hours / 12) #counter = 1 next AM/PM cycle
        new_hours = new_hours % 12
        if new_hours == 0:
            new_hours = 12

    space = start.index(' ')
    oneday = 0
    if counter == 0:
        ampm = start[space:]
    if counter % 2 == 0:
        ampm = start[space:]
    else:
        ampm = start[space:]
        if ampm == ' AM':
            oneday = 0
            ampm = ' PM'
        elif ampm == ' PM':
            oneday = 1
            ampm = ' AM'

    #print('counter', counter)

    if new_minutes >= 0 and new_minutes <=9:
        new_minutes = '0' + str(new_minutes)


    day = day.capitalize()
    #print(day)

    if counter == 1 and oneday == 1:
        next_day = ' (next day)'
    elif counter == 2:
        next_day = ' (next day)'
    elif counter >= 2 and oneday == 1:
        next_day = ' (' + str(int(counter/2) + 1) + ' days later)'
    else:
        next_day = ''

    #print(counter)


    numdays = str((int(counter/2)+1)%7) #number of days past
    #print('numdays =', numdays)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', '']
    #print(weekdays.index(day))
    # d = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday':3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    # #print(d)
    #     adding = weekdays.index(day) + int(numdays)
    #     day = weekdays[adding]
    #     print(day)
    #print(weekdays[0])
    # = weekdays.index(day)
    #print()
    # might need to assign a dictionary for days of the week
    #print(day)

    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday':
        if counter == 1 and oneday == 1:
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + ', ' + day + next_day
            print(answer)
            return(answer)
        elif counter == 2:
            adding = weekdays.index(day) + int(numdays) - 1
            if adding == 7:
                adding = 0
            day = weekdays[adding]
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + ', ' + day + next_day
            print(answer)
            return(answer)
        elif counter >= 2 and oneday == 1:
            adding = weekdays.index(day) + int(numdays)
            if adding == 7:
                adding = 0
            day = weekdays[adding]
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + ', ' + day + next_day
            print(answer)
            return(answer)
        else:
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + ', ' + day
            print(answer)
            return(answer)
    else:
        if counter == 0:
            answer = str(new_hours) + ':' + str(new_minutes) + ampm
            print(answer)
            return(answer)
        if counter == 2:
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + next_day
            print(answer)
            return(answer)
        else:
            answer = str(new_hours) + ':' + str(new_minutes) + ampm + next_day
            print(answer)
            return(answer)

add_time('3:09 PM', '537:30', 'tuesdAy')
