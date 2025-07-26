import datetime as dt
print("today = ",dt.datetime.today().strftime("%Y-%m-%d")) 
# 顯示今天的日期
print("今天日期 = ", dt.datetime.today().strftime("%Y-%m-%d"))

# 顯示目前的時間 (HH:MM:SS)
print("目前時間 (HH:MM:SS) = ", dt.datetime.now().strftime("%H:%M:%S"))

# 顯示目前的時間 (包含毫秒)
print("目前時間 (含毫秒) = ", dt.datetime.now().strftime("%H:%M:%S.%f"))

# 顯示目前時間 (12小時制 AM/PM)
print("目前時間 (12小時制) = ", dt.datetime.now().strftime("%I:%M:%S %p"))

# 顯示目前時間 (24 小時制：HH:MM:SS)
print("目前時間 (24小時制) = ", dt.datetime.now().strftime("%H:%M:%S"))

# 顯示完整的日期和時間
print("完整日期與時間 = ", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 顯示完整的日期和時間 (包含星期幾)
print("完整日期與時間 (含星期) = ", dt.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S"))


print("hello Python")
