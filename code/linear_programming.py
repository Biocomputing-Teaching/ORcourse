""" A function to solve a linear programming problem using OR-Tools library.

Input: 
- solver: A solver object created using pywraplp module of OR-Tools library.
- variable_list: A list of variables used in the problem, created using the NumVar method of the solver object.
- constraint_list: A list of constraints added to the problem, created using the Add method of the solver object.

Output:
- Prints the number of variables and constraints in the problem.
- Solves the problem and prints the optimal solution, time taken, and reduced cost of each variable.
- Prints the dual value and activity level of each constraint. """



from ortools.linear_solver import pywraplp

def ShowResults(solver, variable_list, constraint_list):
    """Solve the problem and print the solution."""
    print('# of variables = %d' % solver.NumVariables())
    print('# of constraints = %d' % solver.NumConstraints())

    result_status = solver.Solve()

    # check results are ok
    assert result_status == pywraplp.Solver.OPTIMAL
    assert solver.VerifySolution(1e-7, True)

    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Optimal objective value = %f' % solver.Objective().Value())
    for variable in variable_list:
        print('%s = %f' % (variable.name(), variable.solution_value()))
    print('Problem solved in %d iterations' % solver.iterations())
    for variable in variable_list:
        print('%s: reduced cost = %f' %
              (variable.name(), variable.reduced_cost()))
    activities = solver.ComputeConstraintActivities()
    for i, constraint in enumerate(constraint_list):
        print(('constraint %d: dual value (shadow price) = %f\n'
               '               final value (activity) = %f' %
               (i, constraint.dual_value(), activities[constraint.index()])))

# Define the solver to use
solver = pywraplp.Solver.CreateSolver('GLOP')

# Define the problem
infinity = solver.infinity()
x1 = solver.NumVar(0.0, infinity, 'x1')
x2 = solver.NumVar(0.0, infinity, 'x2')
   
solver.Maximize(50 * x1 + 60 * x2)
c0 = solver.Add(50 * x1 + 30 * x2  <= 2000, 'Material')
c1 = solver.Add(6 * x1 + 5 * x2  <= 300, 'MachineTime')
c2 = solver.Add(3 * x1 + 5 * x2  <= 200, 'Labor')

ShowResults(solver, [x1, x2], [c0, c1, c2])