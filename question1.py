class HW1Q1:
    def __init__(self,time):
        self.time = time
    def timeConvert(self, input_second):
        sec = 0
        min = 0
        day = 0
        hour = 0
        year = 0
        if int(input_second) // 60 >= 1:
            min = int(input_second) // 60
            sec = int(input_second) % 60
            if min// 60 >= 1:
                hour = min // 60
                min = min % 60
                if hour // 24 >= 1:
                    day = hour // 24
                    hour = hour % 24
                    if  day // 365 >= 1:
                        year = day // 365
                        day = day % 365
        else:
            sec = input_second
        if year != 0:
            print(str(year), "years",str(year), "years",str(day),str(hour), "hour", "day",str(min), "min",str(sec), "sec")
        else:
            if day != 0:
                print(str(day), "day",str(hour), "hour",str(min), "min",str(sec), "sec")
            else:
                if hour != 0:
                    print(str(hour), "hour", str(min), "min", str(sec), "sec")
                else:
                    if min != 0:
                        print(str(min), "min", str(sec), "sec")
                    else:
                        print(str(sec), "sec")

##################################################################

time = input("input a time to be converted (sec): ")
output = HW1Q1(time)
output.timeConvert(time)