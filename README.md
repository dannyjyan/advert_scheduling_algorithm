# Advertisement Scheduling Algorithm

This program implements an advertisement algorithm that gives the jobs done and the order to do them in to guarantee max profit. It uses a greedy algorithm that runs in O(n^2) time.

## How to run it

1. Save the Python file to your computer
2. Run this command:
   ```
   python adversiement_scheduling.py
   ```

# Pseudocode of Algorithm.
```
def advertisement_scheduling(jobs):

    if <Jobs is Empty>:
        return [], 0

    # get max deadline 
    max_deadline = 0
    for job in jobs:
        if job['deadline'] > max_deadline:
            max_deadline = job['deadline']

    if <No slots, slots are non-positive>:
        return [], 0

    # create a list of max_deadline length and initialize it with -1
    schedule = [-1] * max_deadline
    profit = 0

    jobs = <Sort jobs by profit in descending order>

    # iterate through jobs and schedule them
    for job in jobs:
        <Iterate through schedules in reverse order>:
            if <Slot is Open>:
                schedule[i] = job['id']
                profit += job['profit']
                break

    # get rid of -1s in the schedule by making a new list
    schedule = <New List without open slots>

    return schedule, profit
```

# Big O analysis (Step Count/Dominant Terms)
Getting the max_deadline is O(n)
Sorting the jobs in reverse order by deadline is O(nlog(n))
Looping through each job is O(n)
For each job, looping through each slot is O(d), where D is the deadline number
Creating a new list without open slots is O(n)

The bottleneck for this algorithm is looping through the jobs and open slots, which is O(n*d). In the worst case, where every job has a deadline of the last day, then each job has to check at most n different slots,
making this algorith O(n^2).


