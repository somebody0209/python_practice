import datetime

# 常量和函数
DATE_FORMAT = "%Y-%m-%d"
ERROR_MSG_FORMAT = "输入的{}不正确，请重新输入。"
START_DATE_ERROR_MSG = ERROR_MSG_FORMAT.format("起始日期")
END_DATE_ERROR_MSG = ERROR_MSG_FORMAT.format("结束日期")

def get_date_from_input(input_msg, error_msg):
    while True:
        try:
            date_str = input(input_msg)
            date = datetime.datetime.strptime(date_str, DATE_FORMAT)
            return date
        except ValueError:
            print(error_msg)

# 主程序
while True:
    start_date = get_date_from_input("请输入起始日期 (YYYY-MM-DD): ", START_DATE_ERROR_MSG)
    end_date = get_date_from_input("请输入结束日期 (YYYY-MM-DD): ", END_DATE_ERROR_MSG)
    if end_date < start_date:
        print("结束日期必须在开始日期之后，请重新输入。")
        continue
    break

# 使用timedelta计算两个日期之间的天数
delta = end_date - start_date
days = delta.days

# 打印出两个日期之间的天数和去掉时间部分的起始日期和结束日期
print("起始日期: ", start_date.strftime(DATE_FORMAT))
print("结束日期: ", end_date.strftime(DATE_FORMAT))
print("相差天数: ", days)
