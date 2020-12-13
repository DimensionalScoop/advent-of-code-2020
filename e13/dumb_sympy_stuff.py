#%%
import numpy as np
import sympy as s
from sympy.matrices.dense import matrix_multiply_elementwise
from data import buses

schedule = np.array(list([(t, b) for t, b in enumerate(buses) if b != -1]))

def is_solution(departure):
    for t, b in schedule:
        if (departure + t) % b != 0:
            return False
    return True

#%%
# b_i : bus id
# t_i : time of departure relative to first bus
# T : time of departure first bus
# ^1
# (T + t_i) % b_i = 0
# <=> T = b*n-t
# find an n ∈  that produces the smalles T
d = len(schedule[:, 0])
t = s.Matrix(schedule[:, 0])
b = s.diag(*schedule[:,1].tolist())
u = s.Matrix([1] * d)

T = s.symbols("T",integer=True)
n = s.Matrix(s.symbols("n:" + str(d),integer=True))
vars = [T,*n]

#%%
sol = s.linsolve(b*n-t-u*T,*n)
sol
#%%
s.solveset(s.Mod(T+t[1],b[1,1]),T)
#%%
constraint = b*n- t
solveme = list(s.Eq(c,T) for c in constraint)
solveme
#%%
vars = [T,*n]
solution_set = s.linsolve(solveme,vars)
solution_set
#%%

# %%
solutions = []
for left,right in zip(vars,solution_set.args[0]):
    solutions.append(s.Eq(left,right))
solutions

#%%
con = [s.solveset(solveme[i],T,s.S.Naturals) for i in range(d)]

# %%
s.combsimp(con[0])
# %%
# %%
