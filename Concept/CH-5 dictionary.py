 # Dictionary 

 # In the python,a dictionry is a built-in data typy used to store key-value paire .
 #  It's like a real-world dictionary where you look up a work (Key) to get its meaning (value).

my_dict = {
    "name": "Shreya",
    "age": 21,
    "city": "Delhi"
}


#"name","age",and "city" are the keys.
#"Shreya",21,and "Delhi" are the value.

# Key features-

#Unordered (as of Python 3.6+, they preserve insertion order)

#Mutable (you can change, add, or remove items)
#Keys must be unique
#Keys must be immutable (like strings, numbers, or tuples)








 # Dictionary is a coollection of key-value pairs

marks={
  "Harry": 100,
  "ajay": 34,
  "sharma":45,
  "alex":76,
  "niyaati": 89,
  list:[1,2,3,45,7], 
  70:"shubh" ,
  60.7:"shivnsh"
}

#EX---

student = {"name": "Shreya", "score": 95}
print(student["name"])   # Output: Shreya



print(marks,type(marks))

print(marks["Harry"])

# properties of Dictionary'
"""
1. it is  unordered
2. it it is mutubale
3. it is indexed
4.cannot duplicate the keys
"""



m={
  7:"khalessi",
  8:"Eren",
  1:"Tyler",
  2:"Frank",
  0.1:"Jhon snow",
  0.001:"JOJO"

}


#Methods of dict

print(m.items()) # this will display it in the tuples fromat(,)

print(m.values()) #returns with the values 

print(m.keys()) # returs with the keys 
m.update({"Peter Parker":0.0001}) # Updates the disctiionary with supllied key-value pairs

print(m.clear)
print(m)

m.pop(0.001) #removes the specificed key from the dictionary and then return the corresponiding

m.popitem() # Removes and return a pair from the dicitonary. Piars are returned in LIFO 
print (m)


  

