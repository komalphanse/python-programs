print("using add method")
months=set(["january","february","march","april","may","june"])
print(months)
months.add("july")
months.add("august")

months.update(["september","october","november"])
print(months)
for i in months:
    print(i)

print("\n remove items from set") 

months.discard("may")
months.remove("march")
print(months)

print("\n removing all items from set using clear method")
months.clear()
print("\n cleared se=",months)