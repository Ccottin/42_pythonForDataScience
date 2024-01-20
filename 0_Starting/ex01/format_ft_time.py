import time
import datetime

actual_time = time.localtime()
seconds = time.time()
time_scientific = "{:=.2f}e+9".format(seconds / 1e9)
print("Second since January 1, 1970:", f'{seconds:,.4f}', "or", time_scientific, "in scientific notation")

datetime_object = datetime.datetime.strptime(time.strftime("%m", actual_time), "%m")
print(datetime_object.strftime("%b"), time.strftime("%d %Y", actual_time))
