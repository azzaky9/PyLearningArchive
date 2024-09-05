# <variable>[start:endindex]

s = "Hello World!"
# print(len(s))
substring = s[7:12]
print(substring)

hello = s[:5]
print(hello)

world = s[6:]
print(world)

world_minus = s[-6:]
print(world_minus)

world_without_symbol = s[-6:-1]
print(world_without_symbol)

world_only_character_two = s[::2]
print(world_only_character_two)

world_only_char_range = s[1:10:2]
print(world_only_char_range)