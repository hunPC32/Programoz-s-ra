class Subtitle:
    def __init__(self, timing, text):
        self.timing = timing.strip()
        self.text = text.strip()

    def convertTiming(self):
        timeParts = self.timing.split(" - ")

        start = timeParts[0]
        end = timeParts[1]

        return f"{self.convertToHour(start)} --> {self.convertToHour(end)}"

    def convertToHour(self, time):
        temp = time.split(":")
        sec = temp[1]
        min = int(temp[0])
        hour = int(min / 60)
        min = min % 60

        if min < 10:
            min = f"0{min}"
        if hour < 10:
            hour = f"0{hour}"

        return f"{hour}:{min}:{sec}"