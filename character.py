character1_name = str(input("Name the first character "))
character1_level = int(input("Assign a starting level for the first character "))
character1_health = int(input("Assign starting hitpoints for the first character "))
character2_name = str(input("Name the second character "))
character2_level = int(input("Assign a starting level for the second character "))
character2_health = int(input("Assign starting hitpoints for the second character "))
character3_name = str(input("Name the third character "))
character3_level = int(input("Assign a starting level for the third character "))
character3_health = int(input("Assign starting hitpoints for the third character "))

print(character1_name)
print(character1_level)
print(character1_health)
print(character2_name)
print(character2_level)
print(character2_health)
print(character3_name)
print(character3_level)
print(character3_health)

array=[[character1_name, (character1_level, character1_health)],
       [character2_name, (character2_level, character2_health)],
       [character3_name, (character3_level, character3_health)]]

print(array)

if character1_level > character2_level and character1_level > character3_level:
        print(character1_name)
        if character2_level > character3_level:
            print(character2_name)
            print(character3_name)
        else:
         print(character3_name)
         print(character2_name)

if character2_level > character1_level and character2_level > character3_level:
        print(character2_name)
        if character1_level > character3_level:
            print(character1_name)
            print(character3_name)
        else:
         print(character3_name)
         print(character1_name)
         
if character3_level > character1_level and character3_level > character2_level:
        print(character3_name)
        if character2_level > character1_level:
            print(character2_name)
            print(character1_name)
        else:
         print(character1_name)
         print(character2_name)