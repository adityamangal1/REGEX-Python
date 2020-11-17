import re
# Do not delete 'r'.
Regex_Pattern = r"^[0-9]{2}[a-zA-Z-/.]{1}[0-9]{2}[a-zA-Z-/.]{1}[0-9]{4}"


print(str(bool(re.search(Regex_Pattern, input()))).lower())
