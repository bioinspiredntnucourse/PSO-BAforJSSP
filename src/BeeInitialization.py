import random
from Problem import Problem

from Bee import Bee
from Site import Site


def scout_bee_init(num_scout_bees, problem):
    scout_bees = []

    for i in range(num_scout_bees):
        scout_bee = Bee(problem.num_operations)
        scout_bee.site = get_random_site(problem)
        scout_bees.append(scout_bee)

    return scout_bees


def get_random_site(problem):
    num_operations = problem.num_operations
    random_site = Site(num_operations)

    #Create a list of size equal to number of operation, and every operation is marked by a number which equals the job
    job_operation_list = []
    for i in range(problem.num_jobs):
        for j in range(problem.num_machines):
            job_operation_list.append(i)

    for i in range(len(random_site.location)):
        random_operation_nr = random.randint(0, len(job_operation_list)-1)

        # print("random_operation_nr: ", random_operation_nr)
        # print("len(job_operation_list): ", len(job_operation_list))

        random_site.location[i] = job_operation_list[random_operation_nr]
        del job_operation_list[random_operation_nr]

    return random_site
