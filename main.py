from datetime import datetime
from zoneinfo import ZoneInfo
from tzlocal import get_localzone

def convertToJapaneseTime(fullDate, diff):
    timeToConvert = datetime.strptime(fullDate, "%Y-%m-%d %H:%M")
    convertedTime = timeToConvert - diff
    return convertedTime.strftime("%Y/%m/%d %H:%M")

def convertToLocalTime(japaneseTime, diff):
    timeToConvert = datetime.strptime(japaneseTime, "%Y-%m-%d %H:%M")
    convertedTime = timeToConvert + diff
    return convertedTime.strftime("%Y/%m/%d %H:%M")

def main():
    now = datetime.now()

    tzCurrent = get_localzone() 
    tzTokyo = ZoneInfo("Asia/Tokyo")

    offsetCurrent = now.astimezone(tzCurrent).utcoffset()
    offsetTokyo = now.astimezone(tzTokyo).utcoffset()

    diff = offsetTokyo - offsetCurrent

    toJapaneseTime = True

    print("Type 'local' to convert to local time or 'quit' to exit)")
    
    while True:
        if (toJapaneseTime):
            time = input("Convert time to Japanese time (HH:MM): ")
        else:
            time = input("Convert local time to Japanese time (HH:MM): ")

        if time.lower() == "local" and toJapaneseTime:
            toJapaneseTime = False
            print("Now converting to local time.")
            continue
        elif time.lower() == "japan" and not toJapaneseTime:
            toJapaneseTime = True
            print("Now converting to Japanese time.")
            continue

        try:
            if time.lower() == "quit" or time.lower() == "q":
                break

            if (toJapaneseTime):
                fullDate = now.astimezone(tzTokyo).date().isoformat() + " " + time
                convertedTime = convertToJapaneseTime(fullDate, diff)
                print(
                    f"Japan time: {time}\n" 
                    + "           ↓          " 
                    + f"\nYour time: {convertedTime}"
                )
                break
            else: 
                fullDate = now.astimezone(tzCurrent).date().isoformat() + " " + time
                convertedTime = convertToLocalTime(fullDate, diff)
                print(
                    f"Local time: {time}\n" 
                    + "           ↓          " 
                    + f"\nJapan time: {convertedTime}"
                )
                break
        except ValueError:
            print("Invalid time format. Use format like: HH:MM.")

if __name__ == "__main__":
    main()

