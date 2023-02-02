emp=["john",102,"usa"]
dep1=["cs",10]
dep2=["IT",11]
hod_cs=[10,"mr.thorat"]
hod_IT=[11,"mr.bewon"]

print("printing employee data..")
print("name:%s \t  ID:%d \t country:%s"   %(emp[0],emp[1],emp[2]))
print("\n printing department...")
print("department1 \n name: %s \t id: %d" %(dep1[0],dep1[1]))
print("department2 \n name: %s \t id: %d" %(dep2[0],dep2[1]))

print("\n printing HOD details..")
print("hod_id: %d \t hod_name: %s \n hod_IT: %d \t hod_IT: %s" %(hod_cs[0],hod_cs[1],hod_IT[0],hod_IT[1]))
print(type(emp),type(dep1),type(dep2),type(hod_cs),type(hod_IT))