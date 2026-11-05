# Work example 1: JSON round trip
# results {"title": "Hello", "image": null} / True

# import json
# post = {"title": "Hello", "image": None}
# encoded = json.dumps(post)
# decoded = json.loads(encoded)
# print(encoded)
# print(decoded == post)


# Work example 2: A temporary text file
# results Hello, Jomcode

# from pathlib import Path
# from tempfile import TemporaryDirectory
# with TemporaryDirectory() as folder:
#     path = Path(folder) / "draft.txt"
#     with path.open("w", encoding="utf-8") as file:
#         file.write("Hello, JomCode")
#     print(path.read_text(encoding="utf-8"))


# # Work example 3: Configuration defaults
# # results  http://locationhost:5173 / False

# import os
# origin = os.getenv("FRONEND_ORIGIN", "http://locationhost:5173")
# print(origin)
# print(bool(os.getenv("SUPABASE_DB_URL")))


# Work example 4: Check the active interpreter
# example

import sys
from importlib.metadata import PackageNotFoundError, version
print(sys.executable)
try:
    print(version("fastapi"))
except PackageNotFoundError:
    print("FastAPI is not installed in this interpreter")