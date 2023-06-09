# You are a facility manager at a large business center. One of your responsibilities is to check if each conference
# room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number
# of visitors. Each chair will be presented with the char "X". Next, there will be a single space and the number of
# visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more
# chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".
# Input	                Output
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3	                Game On, 4 free chairs left

# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8	            1 more chairs needed in room 2
#                       2 more chairs needed in room 3
number_of_rooms = int(input())
chairs = list
people = list
all_chairs = 0
all_people = 0
for i in range(1, number_of_rooms+1):
    state = input().split(" ")
    chairs = (state[0]).count("X")
    people = int(state[1])
    all_chairs += chairs
    all_people += people
    if chairs < people:
        print(f"{people - chairs} more chairs needed in room {i}")

if all_people <= all_chairs:
    print(f'Game On, {all_chairs - all_people} free chairs left')

