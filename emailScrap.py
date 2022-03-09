import re
import json

with open('websiteData.txt', 'r', encoding="utf-8") as f:
    content = f.read()
    print(content)

#content = "Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com"

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

result = {}

emails = re.findall(regex, content)
print(emails)
human_type_email = r'\b[A-Za-z0-9_%+-]+[.][A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
for email in emails:
    #details dict for occurance and EmailType
    details = {}
    if email not in result.keys():
        human = re.findall(human_type_email,email)
        #print(human)
        details["Occurance"] = 1
        if len(human) != 0:
            details["EmailType"] = "Human"
        else:
            details["EmailType"] = "Non-Human"
        result[f"{email}"] = details
    else:
        result[f"{email}"]["Occurance"] = result[f"{email}"]["Occurance"] + 1

print(result)

with open("result.json", "w") as write_file:
    json.dump(result, write_file, indent=4)