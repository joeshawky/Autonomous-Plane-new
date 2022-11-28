
def pr():
    print("Hi")

def loop(text):
    for i in range(10):
        text


a = 149.16419266323848179847
b = 35.36319236331290380917
a_len = len(str(int(a)))
b_len = len(str(int(b)))

a_rounded = round(a, (12-a_len))
b_rounded = round(b, (12-b_len))

lat1 = str(a_rounded).replace(".", "")[0:5]
lat2 = str(a_rounded).replace(".", "")[5:9]
lon1 = str(b_rounded).replace(".", "")[0:5]
lon2 = str(b_rounded).replace(".", "")[5:9]




# b_without_dot = str(b_rounded).replace(".", "")
def hello_world(a, b, c=1):
    return a, b, c
    

print(hello_world(1, c=3, b=5))

# lat1 = a_without_dot / pow(10, 5)
# print(type(a_without_dot))


# # lita = [["joe", 20], ["miron", 21], ["merve", 16]]
# lita = [1, 2, 3, 4, 5, 6, 7]
# # first = lita[0]
# print(lita[0:3])