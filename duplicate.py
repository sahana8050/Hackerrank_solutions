n=[1,2,3,4,3]
for firstelement in range(len(n)):
    for secondelement in range(firstelement+1,len(n)):
        if n[firstelement]==n[secondelement]:
            print("True")
            exit()
else:
 print("False")




           





