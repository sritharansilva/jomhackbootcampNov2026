# Example 1: Import a standard module
# results draft.json / j.son

# from pathlib import Path
# path = Path("post") / "draft.json"
# print(path.name)
# print(path.suffix)


# Example 2: A class and an instance
# results Hello

# class Post:
#     def __init__(self, title: str):
#         self.title = title.strip()
#     def preview(self) -> str:
#         return self.title[:5]

# post = Post(" Hello world ")
# print(post.preview())



# Example 3: Annotations and optional values
# results No image / a/photo.png


# def image_label(path: str | None) -> str:
#     return "No image" if path is None else path

# print(image_label(None))
# print(image_label("a/photo.png"))


# Example 4: Qualified names and entry points
# results {"ok".true}

# import json
# def main():
#     print(json.dumps({"ok": True}))

# if __name__=="__main__":
#     main()

