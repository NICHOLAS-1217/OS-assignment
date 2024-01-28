class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_waiting_time(processes):
    total_waiting_time = 0
    for process in processes:
        process.waiting_time = process.turnaround_time - process.burst_time
        total_waiting_time += process.waiting_time
    return total_waiting_time

def calculate_turnaround_time(processes):
    total_turnaround_time = 0
    for process in processes:
        process.turnaround_time = process.turnaround_time - process.arrival_time
        total_turnaround_time += process.turnaround_time
    return total_turnaround_time

def priority_scheduling(processes):
    gantt_chart = []
    time = 0
    while processes:
        ready_processes = [process for process in processes if process.arrival_time <= time and process.remaining_time > 0]
        if not ready_processes:
            time += 1
            continue

        ready_processes.sort(key=lambda x: x.priority)
        current_process = ready_processes[0]

        if current_process.remaining_time == current_process.burst_time:
            current_process.start_time = time
        time += 1
        current_process.remaining_time -= 1
        gantt_chart.append(current_process.pid)

        if current_process.remaining_time == 0:
            current_process.turnaround_time = time
            processes.remove(current_process)

    if not gantt_chart:
        total_turnaround_time = 0
        total_waiting_time = 0
        average_turnaround_time = 0
        average_waiting_time = 0
    else:
        total_turnaround_time = calculate_turnaround_time(processes)
        total_waiting_time = calculate_waiting_time(processes)
        average_turnaround_time = total_turnaround_time / len(gantt_chart)
        average_waiting_time = total_waiting_time / len(gantt_chart)

    return gantt_chart, total_turnaround_time, average_turnaround_time, total_waiting_time, average_waiting_time

def display_gantt_chart(gantt_chart):
    print("Gantt Chart:")
    for process in gantt_chart:
        print(f"| P{process} ", end="")
    print("|")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes (3 to 10): "))
    if num_processes < 3 or num_processes > 10:
        print("Number of processes should be between 3 and 10.")
        exit()

    processes = []
    for i in range(num_processes):
        burst_time = int(input(f"Enter burst time for P{i}: "))
        arrival_time = int(input(f"Enter arrival time for P{i}: "))
        priority = int(input(f"Enter priority for P{i}: "))
        processes.append(Process(i, arrival_time, burst_time, priority))

    gantt_chart, total_turnaround_time, avg_turnaround_time, total_waiting_time, avg_waiting_time = priority_scheduling(processes)

    display_gantt_chart(gantt_chart)

    print("\nTurnaround time for each process:")
    for process in processes:
        print(f"P{process.pid}: {process.turnaround_time}")

    print(f"\nTotal Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

    print("\nWaiting time for each process:")
    for process in processes:
        print(f"P{process.pid}: {process.waiting_time}")

    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
