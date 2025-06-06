def advertisement_scheduling(jobs):
    # Jobs = [(id:"A", deadline:3, profit:20)]
    if len(jobs) == 0:
        return [], 0
    # get max deadline 
    max_deadline = 0
    for job in jobs:
        if job['deadline'] > max_deadline:
            max_deadline = job['deadline']

    if max_deadline == 0:
        return [], 0
    # create a list of max_deadline length and initialize it with -1
    schedule = [-1] * max_deadline
    profit = 0
    # sort jobs by profit in descending order 
    jobs.sort(key=lambda x: x['profit'], reverse=True)

    # iterate through jobs and schedule them
    for job in jobs:
        # go through the schedule in reverse order
        for i in range(job['deadline'] - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = job['id']
                profit += job['profit']
                break

    # get rid of -1s in the schedule by making a new list
    schedule = [job for job in schedule if job != -1]

    return schedule, profit
        
if __name__ == "__main__":
    jobs = [
        {'id': 'A', 'deadline': 2, 'profit': 100}, 
        {'id': 'B', 'deadline': 1, 'profit': 19}, 
        {'id': 'C', 'deadline': 2, 'profit': 27}, 
        {'id': 'D', 'deadline': 1, 'profit': 25}, 
        {'id': 'E', 'deadline': 3, 'profit': 15},
    ]
    schedule, profit = advertisement_scheduling(jobs)
    print("Original test case:")
    print(schedule, profit)
    print("\nTest case with all deadlines at last slot:")
    
    # New test case with all deadlines at last slot
    last_slot_jobs = [
        {'id': 'X', 'deadline': 5, 'profit': 50},
        {'id': 'Y', 'deadline': 5, 'profit': 40},
        {'id': 'Z', 'deadline': 5, 'profit': 30},
        {'id': 'W', 'deadline': 5, 'profit': 20},
        {'id': 'V', 'deadline': 5, 'profit': 10},
    ]
    schedule, profit = advertisement_scheduling(last_slot_jobs)
    print(schedule, profit)
    
    print("\nTest case with sparse deadlines (will leave empty slots):")
    sparse_jobs = [
        {'id': 'P', 'deadline': 6, 'profit': 100},  # Will take slot 5
        {'id': 'Q', 'deadline': 4, 'profit': 80},   # Will take slot 3
        {'id': 'R', 'deadline': 2, 'profit': 60},   # Will take slot 1
    ]
    schedule, profit = advertisement_scheduling(sparse_jobs)
    print(schedule, profit)
        
