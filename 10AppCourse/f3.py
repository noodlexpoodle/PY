import datetime

filename = datetime.datetime.now()
formatted = filename.strftime("%y-%m-%d-%H-%M-%S")
print(filename)
def create_file():
    with open(formatted+'.txt','w') as file:
        file.write("hello \n I'm your friend")
print(formatted)
create_file()
