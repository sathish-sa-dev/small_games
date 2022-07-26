## Program: Flames game
## Author: Sathish

user1 = name1 = input("Enter your name: ").lower()
user2 = name2 = input("Enter your partner's name: ").lower()

flames = "FLAMES"
flames_full_form = {"F":"Friends", "L": "Love", "A": "Affection", "M": "Marriage", "E": "Enemies", "S": "Sister/Brother"}

common_characters_count = 0
check_name = name1 if len(name1) < len(name2) else name2
for i in check_name:
    c1 = name1.count(i)
    c2 = name2.count(i)
    name1 = name1.replace(i,"")
    name2 = name2.replace(i,"")
    common_characters_count += c1 if c1 < c2 else c2
common_characters_count = (len(user1) + len(user2)) - (common_characters_count * 2)

i = 1
index = 0
while(len(flames) > 1):
    while True:
        if index >= len(flames):
            index = 0
        if i % common_characters_count == 0:
            flames = flames.replace(flames[index],"")
            break
        i += 1
        index += 1
    i += 1

# print("Count: ",common_characters_count)
print(flames_full_form[flames])
