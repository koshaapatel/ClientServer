import re
# Using readline()
file1 = open('data.txt', 'r')
count = 0
customer={}
# customerdata=[]

while True:
    count += 1
    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    tempdata=line.split("|")

    if(re.findall("[a-z]",tempdata[0].lower()) and tempdata[0]!=''):
        # customerdata=[tempdata[1].lower().strip(),tempdata[2].lower().strip(),tempdata[3].lower().strip()]
        customerdata = [" ".join(tempdata[1].lower().split()), " ".join(tempdata[2].lower().split()), " ".join(tempdata[3].lower().split())]
        customer[tempdata[0].lower().strip()]=customerdata

        for temp in tempdata:
            # print(temp.lower().strip())
            print(" ".join(temp.lower().split()))
            # print("{}".format(line.strip()))
    else:
        print("database record is skipped")

file1.close()

for key in customer.keys():
    if(key=="ahmad"):
        tempdata=customer[key]
        phone = input(" enter phone number: ")
        tempdata[2]=" ".join(phone.lower().split())

        address = input(" enter adress: ")
        tempdata[1] = " ".join(address.lower().split())
        customer[key] = tempdata


print(customer.keys())
print(customer.values())

