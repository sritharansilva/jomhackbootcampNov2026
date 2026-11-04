# Example 1: A reusable preview  
#  result Hello / Hello wo

# def preview(text, limit=5):
#     return text.strip()[:limit]

# print(preview(" Hello world "))
# print(preview(" Hello world ", limit=8))


# Example 2: Return several results
#  result Hi / Welcome

# def clean_fields(title, body):
#     return title.strip(), body.strip()

# title, body = clean_fields(" Hi ", " Welcome ")
# print(title)
# print(body)



# Example 3: Local scope
# result Inside / Outside

# title = "Outside"
# def label():
#     title = "Inside"
#     return title

# print(label())
# print(title)



# Example 4: Guard clauses
# result False / True

# def can_edit(user_id, author_id):
#     if user_id is None:
#         return False
#     return user_id == author_id
# print(can_edit(None, "a"))
# print(can_edit("a", "a"))




# EXERCISE 1: TITLE VALIDATOR


