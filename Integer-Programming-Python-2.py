import pulp
sausage = pulp.LpProblem("Cost minimising blending problem", pulp.LpMinimize)
sausage_types = ['economy', 'premium']
ingredients = ['pork', 'wheat', 'starch']
ing_weight = pulp.LpVariable.dicts("weight kg",
                                     ((i, j) for i in sausage_types for j in ingredients),
                                     lowBound=0,
                                     cat='Continuous')
sausage += (
    pulp.lpSum([
        4.32 * ing_weight[(i, 'pork')]
        + 2.46 * ing_weight[(i, 'wheat')]
        + 1.86 * ing_weight[(i, 'starch')]
        for i in sausage_types])
)
sausage += pulp.lpSum([ing_weight['economy', j] for j in ingredients]) == 350 * 0.05
sausage += pulp.lpSum([ing_weight['premium', j] for j in ingredients]) == 500 * 0.05
sausage += ing_weight['economy', 'pork'] >= (
    0.4 * pulp.lpSum([ing_weight['economy', j] for j in ingredients]))
sausage += ing_weight['premium', 'pork'] >= (
    0.6 * pulp.lpSum([ing_weight['premium', j] for j in ingredients]))
sausage += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) <= 30
sausage += pulp.lpSum([ing_weight[i, 'wheat'] for i in sausage_types]) <= 20
sausage += pulp.lpSum([ing_weight[i, 'starch'] for i in sausage_types]) <= 17
sausage += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) >= 23
sausage.solve()
print('Model Status is ' + pulp.LpStatus[sausage.status])

for var in ing_weight:
    var_value = ing_weight[var].varValue
    print ("The weight of {0} in {1} sausages is {2} kg".format(var[1], var[0], var_value))

total_cost = pulp.value(sausage.objective)

print ("The total cost is ${} for 350 economy sausages and 500 premium sausages".format(round(total_cost, 2)))