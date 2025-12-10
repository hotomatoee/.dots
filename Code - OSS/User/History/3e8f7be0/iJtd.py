from random import randint


words = "hello im a loser"

for x in words:
    print(x)
print(len(words))

if "hello" in words:
    print("yessirski")


b = "hello, i should be practicing math but i much rather would delay and fuck over my life"
print(b[:9])
print(b[9:])

c = "Hello, World!"
print(b[-5:-2])

print(c.upper())
print(c.lower())

whitespace = "       i am so lost, why would i be so lazy            "
print(whitespace.strip())

print(whitespace.replace("i", "you"))

print(c.split(","))

hello = "hello"
world = "world"

outcome = hello + " " + world
print(outcome)

age = 18
txt = f"my name is aidan i am a {age: .2f} year old loser"
print(txt)

txt = "I am \"Aidan\" a fucking loser \n \\n who \r \\r cant even use \t \\t python \b \\b properly \f \\f in the big 25 as a grown adult"
print(txt)


print(9 > 10)
print(9 < 10)

a = randint(0, 100)
b = randint(0, 101)
print(a, b)

if a > b:
    print(a, "larger than", b)
else:
    print(b, "larger than", a)


print(bool(0))
print(bool("hello"))
print(bool(a))

x = int(input("what number do you want to exponentiallise"))

def factorial(x):
    if x == 0 or x == 1:
        return 1 
    else:
        return factorial() * x 
        x -= 1
factorial(x)