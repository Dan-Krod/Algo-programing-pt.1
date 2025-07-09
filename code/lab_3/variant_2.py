names=input("Кому це сподобалось?")
likes=names.split()
print (
    "no one likes this" if  len(likes) == 0 else
    f"{likes[0]} like this" if  len(likes) == 1 else
    f"{likes[0]} and {likes[1]} like this" if len(likes) == 2 else
    f"{likes[0]}, {likes[1]} and {likes[2]} like this" if  len(likes) == 3 else
    f"{likes[0]}, {likes[1]} and {len(likes) - 2} others like this"
    )
