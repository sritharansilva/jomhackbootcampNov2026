# title = " Hello ".strip()
# valid = 1 <= len(title) <= 160
# if valid:
#     print("Ready")
# else:
#     print("Check title")




# Work example 2 chapter 4
# views = 100
# if views == 0:
#     label = "New"
# elif views < 100:
#     label = "Growing"
# else:
#     label = "Popular"
# print(label)


# work example 3 chapter 4
# signed_in = True
# user_id = "user-a"
# author_id = "user-b"
# can_edit = signed_in and user_id == author_id
# print(can_edit)
# print(not signed_in)


# work example 4 chapter 4
# image_path = None
# if image_path is None:
#     print("No image")
# title = ""
# if not title:
#     print("Blank title")
# print(image_path == title)


signed_in = True
user_id = "Sritharan"
author_id = "Sri"
can_edit = signed_in or user_id == author_id
print(can_edit)