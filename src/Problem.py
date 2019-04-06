from Job import Job

class Problem:

    def __init__(self, problem_matrix):
        self.num_jobs = problem_matrix[0][0]
        self.num_machines = problem_matrix[0][1]
        self.num_operations = self.num_jobs * self.num_machines
        self.jobs = []
        for i in range(1, len(problem_matrix)):
            job = Job(i-1, problem_matrix[i])
            self.jobs.append(job)
        if (len(self.jobs) != self.num_jobs):
            print ('Error: Number of job lines are not consistent with number of jobs')

    def __str__(self):
        string = ''
        for job in self.jobs:
            string += 'Job: {}'.format(job.jobNr) + '\n'
            string += job.to_string()
            # print(str)
        return string
