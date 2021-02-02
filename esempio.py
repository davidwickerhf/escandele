from escandele import Room


if __name__ == '__main__':
    # Define here the matrix of the room and create a Room object
    # Call 'calculate_light' on the room object to obtain a converted matrix of light points.


    # Example given in the exercise:
    room_matrix = [['x', 'x', 'x', 'x', 'x'], ['x', 'C', 'X', 'X', 'X'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]
    light_strengh = 3

    # Initialize Room Object
    room = Room(room=room_matrix, l=light_strengh)

    # Print Room
    print('EXAMPLE 1')
    print('Given Room: ')
    for y, xlist in enumerate(room.original_matrix):
        print(f'{y}:  |  {xlist}')

    print(f'\nCalculated Lights (Light strengh: {room.l})')
    for y, xlist in enumerate(room.light_matrix):
        print(f'{y}:  |  {xlist}')
    print(f'\nEmpty Spots Count: {len(room.empty_spots)} | {room.empty_spots}')


    # Or (Example 2)
    print('\n\n')
    room = Room.from_coords(n=5, lights=[(0, 0), (4,4)], l=3)

    # Print Room
    print('\n\nEXAMPLE 2')
    print('Given Room: ')
    for y, xlist in enumerate(room.original_matrix):
        print(f'{y}:  |  {xlist}')

    print(f'\nCalculated Lights (Light strengh: {room.l})')
    for y, xlist in enumerate(room.light_matrix):
        print(f'{y}:  |  {xlist}')
    print(f'\nEmpty Spots Count: {len(room.empty_spots)} | {room.empty_spots}')


    # Or (Example 3)
    print('\n\n')
    room = Room.from_coords(n=8, lights=[(4, 4), (0,7)], l=6)

    # Print Room
    print('\n\nEXAMPLE 3')
    print('Given Room: ')
    for y, xlist in enumerate(room.original_matrix):
        print(f'{y}:  |  {xlist}')

    print(f'\nCalculated Lights (Light strengh: {room.l})')
    for y, xlist in enumerate(room.light_matrix):
        print(f'{y}:  |  {xlist}')
    print(f'\nEmpty Spots Count: {len(room.empty_spots)} | {room.empty_spots}')