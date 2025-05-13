a = '''Dear <|Name|> ,
You are selected!
<|Date|>'''

# print(a.replace("<|Name|>","Mahy").replace("<|Date|>","14 November 2024")) # Chain replace
m=a.replace("<|Name|>","Mahy")
c=a.replace("<|Date|>","14 November 2024")
print(m+c)