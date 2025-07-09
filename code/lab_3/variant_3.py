def like(name_likes) :
       return ( 
            "No one likes this !!!" if  len(name_likes) == 0 else
             f"{name_likes[0]} like this" if  len(name_likes) == 1 else
             f"{name_likes[0]} and {name_likes[1]} like this." if len(name_likes) == 2 else
             f"{name_likes[0]}, {name_likes[1]} and {name_likes[2]} like this." if  len(name_likes) == 3 else
             f"{name_likes[0]}, {name_likes[1]} and {len(name_likes) - 2} others like this."
             )

print(like([]))
print(like(["Peter"]))
print(like(["Jacob", "Alex"]) )
print(like(["Max","John","Mark"]))
print(like(["Alex", "Jacob", "Mark", "Max", "Petro"])) 