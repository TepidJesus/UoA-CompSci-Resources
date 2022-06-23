
"""
A handy calculator to measure the processing time for a given set of processes.

1. Enter the processing time required for each process in their starting order.
2. Once all processes have been entered, press 0 to move to the next stage.
3. Enter the alloted time slice for your machine.
4. Enter the switching time for your machine.
"""


process_times = {}
n = 1
user_in = int(input(f"Enter a The Required Processing Time (ms) For Process {n} (Enter 0 To Move On): "))
while user_in != 0:
    process_times[n] = user_in
    n += 1
    user_in = int(input(f"Enter a The Required Processing Time (ms) For Process {n} (Enter 0 To Move On): "))

time_slice = int(input(f"Enter The Process Time Slice (ms): "))
switching_time = int(input(f"Enter The Switching Time (ms): "))

finished_processes = []
cpu_time = switching_time
running = True
min_time = sum(process_times.values())
while len(finished_processes) != len(process_times.keys()):

    for i in range(1, len(process_times.keys()) + 1):
        if process_times[i] == None:
            continue
        elif process_times[i] <= time_slice:

            cpu_time += time_slice
            finished_processes.append((i, cpu_time))
            process_times[i] = None

            cpu_time += switching_time
        else:

            process_times[i] -= time_slice
            cpu_time += time_slice

            cpu_time += switching_time

highest_time = 0
for process in finished_processes:
    if process[1] > highest_time:
        highest_time = process[1]
    print(f"Process {process[0]} Finished At {process[1]}ms")

effeciency = round(((min_time / highest_time) * 100), 1)

print(f"The Effeciency Is {effeciency}%")