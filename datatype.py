name= input("enter your name:")
gadget= input("enter your favorite gadget:")
agent_number= 7
weight= 37.5
is_active= True
print("data type of agent_number:",type(agent_number))
print("data type of weight:",type(weight))
print("data type of is_active:",type(is_active))
print("data type of name:",type(name))
print("after typecasting")
weight= int(weight)
agent_number= str(agent_number)
print("data type of agent_number:",type(agent_number))
print("data type of weight:",type(weight))
print(name[0:4])
print("reverse of",name)
print(name[::-1])
print(agent_number + " " +name + " ")