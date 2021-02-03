from escandele import Room


if __name__ == '__main__':
    # Define here the matrix of the room and create a Room object
    # Call 'calculate_light' on the room object to obtain a converted matrix of light points.

    # Or (Example 3)
    print('\n\n')
    room = Room.from_coords(n=10, lights=[(0, 0), (9, 9), (5, 5)], l=3)

    # Print Room
    print('\n\nEXAMPLE 3')
    print('Given Room: ')
    for y, xlist in enumerate(room.original_matrix):
        print(f'{y}:  |  {xlist}')

    print(f'\nCalculated Lights (Light strengh: {room.l})')
    for y, xlist in enumerate(room.light_matrix):
        print(f'{y}:  |  {xlist}')
    print(f'\nEmpty Spots Count: {len(room.empty_spots)}')