def read_file(filepath):
    file = open(filepath, "r")
    return file

def read_problem(filename):
    filepath = '..\\problems\\' + filename + '.txt'
    problem_txt = read_file(filepath)

    problem = []

    #Orders the problem into a matrix
    for line in problem_txt:
        if line != '\n':
            job = []
            line = line.replace('\n', '')
            line = line.split(" ")
            for element in line:
                if element != '' and element != '\n':
                    job.append(int(element))
            problem.append(job)

    return problem
