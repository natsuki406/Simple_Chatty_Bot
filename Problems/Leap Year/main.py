# put your python code here
years = int(input())
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
