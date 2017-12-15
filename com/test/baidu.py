import re

content = "Extra things hello 123455 World_this is a regex Demo extra things"

content = re.sub('(\d+)', r'\l 7890', content)
print(content)
