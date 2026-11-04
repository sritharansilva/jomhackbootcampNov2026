# Example 1 : Number each post

# title = ["Hello", "Launch"]
# for number, title in enumerate(title, start=1):
#     print(f"{number}. {title}")


# Example 2: Filter and transform
# posts = [{"title": "Hello", "views":2},
#          {"title": "Launch", "views":12}]
# popular = [p["title"].upper() for p in posts
#            if p["views"] >= 10]
# print(popular)

# Example 3:A bounded while loop
# attempt = 0
# while attempt < 3:
#     attempt +=1
#     print(f"Attempt {attempt}")


# Example 4 : Totals and early exit
# views = [3, 0, 7]
# total = 0
# for value in views:
#     total += value
# print(total)
# for value in views:
#     if value ==0:
#         print("Unvieved post found")
#         break
    