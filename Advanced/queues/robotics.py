from collections import deque


def get_time_after_processing(time: str, sec: int) -> str:
    hour, minutes, seconds = time.split(':')
    total_second = sec + int(hour) * 3600 + int(minutes) * 60 + int(seconds)

    hour = total_second // 3600
    total_second %= 3600
    minutes = total_second // 60
    total_second = total_second % 60
    seconds = total_second

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if hour < 10:
        hour = f"0{hour}"

    return f"{hour}:{minutes}:{seconds}"


robots = deque(input().split(';'))
starting_time = input()
products = deque()
is_last_robot = False

product = input()
while not product == "End":
    products.append(product)
    product = input()

flag = False
while products:
    item = products.popleft()
    robot = robots.popleft()
    robot_name, process_time = robot.split('-')
    out_line_time = ""

    if len(robots) >= 1 and not flag:
        out_line_time = get_time_after_processing(starting_time, 1)
    elif flag:
        out_line_time = get_time_after_processing(starting_time, int(process_time))
        robots.appendleft(robot)
    else:
        flag = True
        out_line_time = get_time_after_processing(starting_time, 1)
        products.appendleft(item)
        robots.appendleft(robot)

    print(f"{robot_name} - {item} [{out_line_time}]")
    starting_time = out_line_time
