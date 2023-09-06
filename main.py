# write your code here
person = {
    "name" : "reemas",
    "age": 17,
    "hobbies": ["reading", "watching_movies", "sleep"]
}
print(person.get("name"))
print(person["age"])

person["age"]= 18

person["country"]="kuwait"

print(person)
print(person.keys)

print(len(person))


person["hobbies"].append("gaming")

def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZING")

check_hobbies(person)