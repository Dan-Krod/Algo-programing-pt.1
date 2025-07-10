def name(likes) :
       if  len(likes) == 0:
             return "no one likes this"
       elif len(likes) == 1:
             return f"{likes[0]} like this"
       elif len(likes) == 2 :
             return f"{likes[0]} and {likes[1]} like this"
       elif len(likes) ==3:
            return f"{likes[0]}, {likes[1]} and {likes[2]} like this"
       else:
            return f"{likes[0]}, {likes[1]} and {len(likes)-2} others like this"

print(name([]))
print(name(["Peter"]))
print(name(["Jacob", "Alex"]) )
print(name(["Max","John","Mark"]))
print(name(["Alex", "Jacob", "Mark", "Max", "Petro"])) 