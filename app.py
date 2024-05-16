import csv
import sys

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data


def main():
    if len(sys.argv) != 3:
        exit()
    
    notasData = read_csv(sys.argv[1])
    roomsData = read_csv(sys.argv[2])

    # Remove Trash from first data
    roomsData[0][0] = roomsData[0][0][roomsData[0][0].find('2'):]
    notasData[0][0] = notasData[0][0][notasData[0][0].find('2'):]


    idsPerRoom = {}
    for line in roomsData:
        # Add Room to dictionary
        room = line[len(line)-1]
        if room not in idsPerRoom:
            idsPerRoom[room] = []

        # Add id to Room
        id = line[0]
        idsPerRoom[room].append(id)

    gradesPerRoom = {}
    for room in idsPerRoom:
        # Add Room to dictionary
        if room not in gradesPerRoom:
            gradesPerRoom[room] = []
        
        # Add each grade to the right room
        for grade in notasData:
            # Skip Unwanted
            if grade[len(grade)-1] in ["F", "RF", ""]: continue
            
            # Find Right Student
            for student in idsPerRoom[room]:
                if student == grade[0]:            
                    # Add it's grade to the room
                    gradesPerRoom[room].append(grade[2:])
    
    # Store grade in a CSV file per Room
    for room in gradesPerRoom:
        data = gradesPerRoom[room]
        with open(room + '.csv', 'w') as file:
            for line in data:
                file.write(';'.join(line))
                file.write('\n')
    
    # Store all grade in a CSV file
    with open("all" + '.csv', 'w') as file:
        for _, roomData in gradesPerRoom.items():
            for line in roomData:
                file.write(';'.join(line))
                file.write('\n')

    # Store all grade in a CSV file except B116
    with open("all-B116" + '.csv', 'w') as file:
        for room, roomData in gradesPerRoom.items():
            if room == "B116": continue
            for line in roomData:
                file.write(';'.join(line))
                file.write('\n')           


if __name__ == "__main__":
    main()
