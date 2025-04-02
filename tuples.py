# a tuple is a collection of items just like a list but with difference like:
# .immutable : can not be changed once made or sliced or modified 
# .the elements in it are ordered ,which means they are in a specific order 
# ,contains all dat types 


example=(1,2,3,"apple",2.5)
print(example)
print(type(example))
print(example[0])
print(example[3])
print(example[1:-1])
print(len(example))

# concatation and repetions
# concatation :
new_tuple= example + (4,5,"banana")
print(new_tuple)

# repetition
repeated = example * 2
print(repeated)


# LISTS is AN  ordered collection of items 
# list are mutable


