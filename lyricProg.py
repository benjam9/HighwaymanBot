# lyricProg

h = open("highwayman.txt")
a = open("americanRemains.txt")
hLyrics = []
aLyrics = []

for line in h:
    hLyrics.append(line)
h.close()
for line in a:
    aLyrics.append(line)
a.close()

lyrics = hLyrics + aLyrics
