import json
with open('some_text_file.txt', encoding= 'utf-8') as f:
    # Read first line to get started.
    print(f.tell())
    one_line = f.readline()
    # Keep reading one line at a time until there are no more.
    while one_line:
        print(one_line[:-1], f.tell())
        one_line =  f.readline()


like = True;

mapL = {"media":{
    "hello": json.dumps(like),
    "bye": 2
}}

print(mapL)