from subtitle import Subtitle


f = open("feliratok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

subtitles = []

timingTemp = ""
for line in lines:
    if timingTemp == "":
        timingTemp = line
    else:
        subtitle = Subtitle(timingTemp, line)
        subtitles.append(subtitle)
        timingTemp = ""

test = subtitles[0]

f = open("felirat.srt", "w", encoding="utf-8")

counter = 1
for subtitle in subtitles:
    f.write(f"{str(counter)}\n")
    f.write(f"{subtitle.convertTiming()}\n")
    f.write(f"{subtitle.text}\n")
    counter += 1
f.close()