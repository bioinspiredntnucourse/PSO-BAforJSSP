from Bee import Bee

def make_schedule(bee, problem):
    site = bee.site
    schedule = Schedule(site, problem)
    return schedule

class Schedule:

    def __init__(self, site, problem):
        self.schedule = []
        for i in range(problem.num_machines):
            self.schedule.append([])

        operation_counter = []
        operation_time = []
        for i in range(problem.num_jobs):
            operation_counter.append(0)
            operation_time.append(0)

        for jobNr in site.location:
            operation = problem.jobs[jobNr].operations[operation_counter[jobNr]]
            operation_counter[jobNr] += 1

            if operation_time[jobNr] > len(self.schedule[operation.machine]):
                time_difference = operation_time[jobNr] - len(self.schedule[operation.machine])
                for j in range(time_difference):
                    self.schedule[operation.machine].append(-1)

            for k in range(operation.time):
                self.schedule[operation.machine].append(jobNr)
            operation_time[jobNr] = len(self.schedule[operation.machine])

    def __str__(self):
        string = ''
        for machine in self.schedule:
            for jobNr in machine:
                if jobNr != -1:
                    string += str(jobNr)
                else:
                    string += ' '
            string += '\n'
        return string


    # def validate_schedule(self):
    #     for i in range(len())
