from string import Template

s = Template("My name is $name, i live in $domicile")
result = s.substitute(name="Zaky", domicile="Medan")
print(result)

example = """
dsakdasdhaskldjasjddasdasldlasdjklasjdl
kajskldaklsdjldhasdjasdhklasjdjas
djasdjaklsjdklasjdjaskldjklasjldkjsa

dasjldjaskldjklasjdklasjdlkasj


dasdaskldjalks

dasjdklasjdasjd
dasjdaksdksaks
dasldkalskdlas


dajskdasljdalskdas

"""

print(example)