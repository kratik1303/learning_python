## So everything is object in python 
# Every object has -->
   # unique identity.
   # unique type
   #unique val

#mutable and immutable objects are always checked with the identity .. 
# If same identity even after crud operations then it is mutable otherwise immutable.

sugar_amt =2 
print (f"Initial value of sugar amount as :{sugar_amt}")
print (f"Initial identity of sugar amount as :{id(sugar_amt)}")
print (f"Initial identity of sugar amount as :{id(2)}")
sugar_amt =12
print (f"After value of sugar amount as :{sugar_amt}")
print (f"After identity of sugar amount as :{id(sugar_amt)}")
print (f"After identity of sugar amount as :{id(12)}")


## so identity of two numbers are different so they are immutable 
# lets check on set

spice_mix = set()
print(f"Initial value of set is :{spice_mix}")
print(f"Initial identity of set is :{id(spice_mix)}")
spice_mix.add("ginger")
spice_mix.add("sugar")
spice_mix.add("tea")
spice_mix.add("milk")
print(f"After value of set is :{spice_mix}")
print(f"After identity of set is :{id(spice_mix)}")
