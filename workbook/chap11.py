# Work example 1: Parts of a URL
# results   http localhost 8000 / /posts  / {'limit': ['2']}

# from urllib.parse import urlparse, parse_qs
# url = urlparse("http://localhost:8000/posts?limit=2")
# print(url.scheme, url.hostname, url.port)
# print(url.path)
# print(parse_qs(url.query))



# Work example 2: Methods and intent
# results -  GET read /  POST create  / PUT replace/update / DELETE remove

# operations = {"GET": "read", "POST": "create",
#               "PUT": "replace/update", "DELETE": "remove"}
# for method, intent in operations.items():
#     print(method, intent)



# Work example 3: Status and body
# results  Hello /  False

# import json
# status = 201
# body = '{"id": "p1", "title": "Hello"}'
# if 200 <= status <300:
#     post = json.loads(body)
#     print(post["title"])
# print(status == 204)




# Work example 4: Headers and origins
# results  application/json     /   False

# headers = {"Content-Type": "application/json"}
# origin = "http://localhost:5173"
# api_origin = "http://localhost:8000"
# print(headers["Content-Type"])
# print(origin == api_origin)


