from collections import Counter, defaultdict
"""
Advent of Code 2018

https://adventofcode.com/2018/day/4

--- Day 4: Repose Record ---

You've sneaked into another supply closet - this time, it's across from the
prototype suit manufacturing lab. You need to sneak inside and fix the issues
with the suit, but there's a guard stationed outside the lab, so this is as
close as you can safely get.

As you search the closet for anything that might help, you discover that
you're not the first person to want to sneak in. Covering the walls, someone
has spent an hour starting every midnight for the past few months secretly
observing this guard post! They've been writing down the ID of the one guard
on duty that night - the Elves seem to have decided that one guard was enough
for the overnight shift - as well as when they fall asleep or wake up while
at their post (your puzzle input).

For example, consider the following records, which have already been organized
into chronological order:

[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up

Timestamps are written using year-month-day hour:minute format. The guard
falling asleep or waking up is always the one whose shift most recently
started. Because all asleep/awake times are during the midnight hour
(00:00 - 00:59), only the minute portion (00 - 59) is relevant for those
events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....

The columns are Date, which shows the month-day portion of the relevant day;
ID, which shows the guard on duty that day; and Minute, which shows
the minutes during which the guard was asleep within the midnight hour.
(The Minute column's header shows the minute's ten's digit in the first row
and the one's digit in the second row.) Awake is shown as ., and asleep is
shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count
as awake on the minute they wake up. For example, because Guard #10 wakes up at
00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time,
you might be able to trick that guard into working tonight so you can have
the best chance of sneaking in. You have two strategies for choosing the best
guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does
that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50
minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
(10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas
any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are
in the order you found them. You'll need to organize them before they can be
analyzed.

What is the ID of the guard you chose multiplied by the minute you chose?
(In the above example, the answer would be 10 * 24 = 240.)

Your puzzle answer was 26281.


--- Part Two ---

Strategy 2: Of all guards, which guard is most frequently asleep on the same
minute?

In the example above, Guard #99 spent minute 45 asleep more than any other
guard or minute - three times in total. (In all other cases, any guard spent
any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose?
(In the above example, the answer would be 99 * 45 = 4455.)

Your puzzle answer was 73001.
"""

def parse_guard_logs(logs_as_strings):
    guard_logs = defaultdict(list)
    current_guard = None
    sleep_start = tuple()
    for entry in sorted(logs_as_strings):
        # print(entry)
        timestamp, event = entry.strip("[").split("] ")
        date, time = timestamp.split()
        year, month, day = tuple(int(each) for each in date.split("-"))
        hour, minute = tuple(int(each) for each in time.split(":"))
        if event == "falls asleep":
            sleep_start = (year, month, day, hour, minute)
        elif event == "wakes up":
            sleep_end = (year, month, day, hour, minute)
            guard_logs[current_guard].append((sleep_start, sleep_end))
        else:
            current_guard = int(event.split()[1].strip("#"))

    return guard_logs


def find_most_minutes_most_frequent_minute(guard_logs):
    guard_logs = parse_guard_logs(guard_logs)
    guard_logs = {guard_id: [m
                             for sleep in [list(range(start[-1], end[-1]))
                                           for start, end in sleeps]
                             for m in sleep]
                  for guard_id, sleeps in guard_logs.items()}
    guard_logs_sleep_minutes = {guard_id: len(sleeps)
                                for guard_id, sleeps in guard_logs.items()}
    sleepiest_guard = max(guard_logs_sleep_minutes.items(),
                          key=lambda g: g[1])[0]
    most_frequent_minute = max(guard_logs[sleepiest_guard],
                               key=guard_logs[sleepiest_guard].count)
    return sleepiest_guard * most_frequent_minute


def find_most_frequent_minute(guard_logs):
    guard_logs = parse_guard_logs(guard_logs)
    guard_logs = {guard_id: [m
                             for sleep in [list(range(start[-1], end[-1]))
                                           for start, end in sleeps]
                             for m in sleep]
                  for guard_id, sleeps in guard_logs.items()}
    guard_logs_sleepiest_minute = {guard_id: Counter(sleeps).most_common(1)[0]
                                   for guard_id, sleeps in guard_logs.items()}
    sleepiest_minute = max(guard_logs_sleepiest_minute.items(),
                           key=lambda g: g[1][1])
    return sleepiest_minute[0] * sleepiest_minute[1][0]


def main():
    guard_logs = []
    with open('day_4_guard_logs.txt', 'r') as log_file:
        guard_logs = log_file.read().splitlines()

    strategy_1 = find_most_minutes_most_frequent_minute(guard_logs)
    print(f"Strategy 1 (guard id * sleepiest minute): {strategy_1}")
    strategy_2 = find_most_frequent_minute(guard_logs)
    print(f"Strategy 2 (guard id * sleepiest minute): {strategy_2}")

if __name__ == '__main__':
    main()
