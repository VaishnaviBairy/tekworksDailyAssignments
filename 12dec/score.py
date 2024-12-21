project = int(input("Enter the project score: "))
internal = int(input("Enter the internal score: "))
external = int(input("Enter the external score: "))
if project >= 50 and internal >= 50 and external >= 50:
    total = (0.7 * project) + (0.1 * internal) + (0.2 * external)
    if total > 90:
        print("Grade A")
    elif total >= 80:
        print("Grade B")
    elif total >= 50:
        print("Grade C")
    else:
        print("Failed")
else:
    if project < 50:
        print(f"You failed in project. Score: {project}")
    if internal < 50:
        print(f"You failed in internal. Score: {internal}")
    if external < 50:
        print(f"You failed in external. Score: {external}")


