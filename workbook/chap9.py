# Work example 1: Handle a known conversion error
# results 12 / None

# def parse_count(text):
#     try:
#         return int(text)
#     except ValueError:
#         return None

# print(parse_count("12"))
# print(parse_count("twelve"))


# Work example 2: Raise a useful error
# results  Title is required

# def clean_title(text):
#     title = text.strip()
#     if not title:
#         raise ValueError("Title is required")
#     return title

# try:
#     clean_title("  ")
# except ValueError as error:
#     print(error)


# work example 3 : Boundry assertions
# results 3 checks passed

# def allowed_size(size):
#     return 0 < size <= 5 * 1024 * 1024

# assert not allowed_size(0)
# assert allowed_size(5 * 1024 * 1024)
# assert not allowed_size(5 * 1024 * 1024 + 1)
# print("3 checks passed")



# Work example 4: Inspect Intermediate values
# results '  Hello  ' 9 / 'Hello' 5

# raw = "  Hello  "
# cleaned = raw.strip()
# print(repr(raw), len(raw))
# print(repr(cleaned), len (cleaned))
# assert len(cleaned) == 5


# EXERSICE 1: NONNEGATIVE COUNTS





# EXERCISE 2: REGRESSION CHECKS


