import datetime
lks = datetime.datetime.now()
st = lks.hour

if 6 <= st < 12:
    sv = "Labrīt!"
elif 12 <= st < 18:
    sv = "Labdien!"
else:
    sv = "Labvakar!"
print(sv)