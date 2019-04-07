from Operation import Operation

class Job:

    def __init__(self, jobNr, problem_line):
        self.operations = []
        for i in range(0,len(problem_line), 2):
            machine = problem_line[i]
            time = problem_line[i+1]
            operationNr = int(i/2)
            operation = Operation(machine, time, operationNr)
            self.jobNr = jobNr
            self.operations.append(operation)

    def __str__(self):
        string = ''
        for operation in self.operations:
            string += 'Operation number: {}'.format(operation.operationNr) + ' \n'
            string += '\t Machine: {}'.format(operation.machine) + '\n'
            string += '\t Time   : {}'.format(operation.time) + '\n'
        return string

    def to_string(self):
        string = ''
        for operation in self.operations:
            string += str(operation)
        return string
