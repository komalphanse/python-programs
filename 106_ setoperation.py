print("\n using union operator")
days1=set({"monday","tuesday","wedensday","turseday"})
days2=set({"friday","saturday","sunday","monday"})
print(days1|days2)
print("\n using union method")
d1={1,2,3,4}
d2={4,5,6,7,3}
d3={8,9,3}
print(d1.union(d2))

print("\n intersection of two sets using intersection operator")
print(days1&days2)
print("\n intersection of two sets using intersection method")
print(d1.intersection(d2))

d1.intersection_update(d2,d3)
print(d1)

print("\n using substraction (-) operator")
print(days2-days1)

print("\n using difference method\n",days2.difference(days1))