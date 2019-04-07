from ReadProblem import read_problem
from RealizeSchedule import plot_schedule
from BeeInitialization import scout_bee_init
from Schedule import Schedule, make_schedule

from Operation import Operation
from Job import Job
from Problem import Problem
from Bee import Bee

def main():
    problem_matrix = read_problem('1')
    problem = Problem(problem_matrix)
    #print(problem)

    scout_bees = scout_bee_init(1, problem)
    print(scout_bees[0])
    # print(problem.jobs[2].operations[0].time)

    schedule = make_schedule(scout_bees[0], problem)
    print(schedule)
    #plot_schedule(problem.num_jobs)

main()
