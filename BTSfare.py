stations = [
  'หมอชิต', 'สะพานควาย', 'อารีย์', 'สนามเป้า', 'อนุสาวรีย์ชัยสมรภูมิ', 'พญาไท',
  'ราชเทวี', 'สยาม', 'ชิดลม', 'เพลินจิต', 'นานา', 'อโศก', 'พร้อมพงษ์',
  'ทองหล่อ', 'เอกมัย', 'พระโขนง', 'อ่อนนุช', 'บางจาก', 'ปุณณวิถี', 'อุดมสุข',
  'บางนา', 'แบริ่ง'
]





# Write a program that calculate the fares from
# input starting and terminal stations.

# The program should be able to =>
# 1. Calculate and print out fares.
# 2. If the input station name is invalid, show error.

# Ex. fare('หมอชิต','แบริ่ง') = 47

# <================WRITE YOUR CODE HERE==================>




def fare(departure, terminal):
    numDe = stations.index(departure)
    numTe = stations.index(terminal)

    numStations = numTe - numDe + 1
    print("Number of stations: ", numStations)

    if numStations == 1 or numStations == 0:
        print("The fare is : 17")
    elif numStations == 2:
        print("The fare is : 25")

        
  


departure = input('Starting station:')
terminal = input('Terminal station:')

fare(departure, terminal)