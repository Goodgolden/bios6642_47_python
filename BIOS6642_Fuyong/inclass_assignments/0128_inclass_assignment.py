start_hour = 9
start_minute = 32
start_second = 50
length_hour = int(input('Please enter hour: '))
length_minute = int(input('Please enter minute: '))
length_second = int(input('Please enter second: '))
end_second = (start_hour + length_hour) * 3600 + (start_minute + length_minute) * 60 + (start_second + length_second)
end_hour = end_second // 3600
end_second = end_second % 3600
end_minute = end_second // 60
end_second = end_second % 60
print(end_hour, end_minute, end_second, sep=':')
