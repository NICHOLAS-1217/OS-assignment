def preemptive_priority():
    total_processes = int(input("Enter the number of processes: "))
    process_list = []

    for i in range(total_processes):
        process_id = "p" + str(i)
        burst_time = int(input(f"Enter burst time for {process_id}: "))
        arrival_time = int(input(f"Enter arrival time for {process_id}: "))
        priority = int(input(f"Enter priority for {process_id}: "))
        process_list.append([process_id, burst_time, arrival_time, priority])

    process_list.sort(key=lambda x: (x[2], x[3], x[1], x[0]))

    current_time = 0
    waiting_time = [0] * total_processes
    turnaround_time = [0] * total_processes
    gantt_chart = []

    while True:
        ready_processes = [process for process in process_list if process[2] <= current_time]
        if not ready_processes:
            break

        ready_processes.sort(key=lambda x: (x[3], x[2], x[1], x[0]))
        current_process = ready_processes[0]

        gantt_chart.append([current_process[0], current_time])
        current_time += 1
        current_process[1] -= 1

        if current_process[1] == 0:
            turnaround_time[int(current_process[0][1:])] = current_time - current_process[2]
            waiting_time[int(current_process[0][1:])] = turnaround_time[int(current_process[0][1:])] - current_process[1]
            process_list.remove(current_process)
        else:
            for process in process_list:
                if process[2] > current_time:
                    break
                if process[3] > current_process[3] and process[1] < current_process[1]:
                    break

            process_list.remove(current_process)
            process_list.append(current_process)

    print("\nTurnaround Time:")
    for process in process_list:
        print(f"{process[0]}: {turnaround_time[int(process[0][1:])] if int(process[0][1:]) < total_processes else 'N/A'}")

    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / total_processes
    print(f"\nTotal Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

    print("\nWaiting Time:")
    for process in process_list:
        print(f"{process[0]}: {waiting_time[int(process[0][1:])] if int(process[0][1:]) < total_processes else 'N/A'}")

    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / total_processes
    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")

    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"{entry[0]} ({entry[1]} - {entry[1] + 1})", end=" | ")


# Example usage
preemptive_priority()
