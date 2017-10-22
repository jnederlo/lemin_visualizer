
num_ants = 0

def take_input():
    with open("input2.txt") as f:
        input = [ line.split() for line in f ]
        # input = [ line.split('-') for line in f ]
    print input
    input_arr = [0 for x in range(len(input) -1)]
    print
    num_ants = input[0][0]
    print "num_ants = ", num_ants
    word = "##start"
    z = 0
    j = 0
    k = 0
    myiter = iter(range(1, len(input)))
    for i in myiter:
        if "##start" in input[i]:
            i += 1
            # print input[i]
            input_arr[j] = room(input[i][0], input[i][1], input[i][2], z, True, False)
            print input_arr[j].name, input_arr[j].x, input_arr[j].y, input_arr[j].z, input_arr[j].s, input_arr[j].e 
            room.num_rooms += 1
            next(myiter, None)
        elif "##end" in input[i]:
            i += 1
            # print input[i]
            input_arr[j] = room(input[i][0], input[i][1], input[i][2], z, False, True)
            print input_arr[j].name, input_arr[j].x, input_arr[j].y, input_arr[j].z, input_arr[j].s, input_arr[j].e 
            room.num_rooms += 1
            next(myiter, None)
        elif "#" in input[0]:
            next(myiter, None)
        elif "-" in str(input[i]) and "L" not in str(input[i]):
            link = str(input[i]).split('-')
            k = 0
            for input_arr[k].name in range(room.num_rooms):
                # print "input_arr[k] = ", input_arr[k]
                if str(input_arr[k].name) == str(link[0][2]):
                    input_arr[k].
                    print "name = ", input_arr[k].name, "k = ", k
                k += 1
        elif "L" in str(input[i]):
            print input[i]
        elif not input[i]:
            pass
        else:
            input_arr[j] = room(input[i][0], input[i][1], input[i][2], z, False, False)
            print input_arr[j].name, input_arr[j].x, input_arr[j].y, input_arr[j].z, input_arr[j].s, input_arr[j].e
            room.num_rooms += 1
        z += 1
        j += 1
    return (input)

def setup():
    size(500, 500)
    input = take_input()
    
    
class room:
    
    num_ants = 0
    num_rooms = 0
    
    def __init__(self, name, x, y, z, s, e):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.s = s
        self.e = e

class links:
    def __init__(self, link):
        self.link = link