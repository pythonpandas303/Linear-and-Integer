import pulp
sales = pulp.LpProblem("Direct_Marketing", pulp.LpMaximize)
i = pulp.LpVariable("phone",0,None,pulp.LpInteger)
j = pulp.LpVariable("direct",0,None,pulp.LpInteger)
sales += 2.4 * i + 9.3 * j, "dollars_collected"
sales += 8 * i + 18 * j <= 420, "time"
sales.writeLP("DirectMarketing.lp")
sales.solve()
print(pulp.LpStatus[sales.status])
for x in sales.variables():
    print(x.name, "=", x.varValue)
print('Totalcommission:$'+str(pulp.value(sales.objective)))

sales2 = pulp.LpProblem("Direct_Marketing",pulp.LpMaximize)
i = pulp.LpVariable("phone",0,None,pulp.LpInteger)
j = pulp.LpVariable("direct",0,None,pulp.LpInteger)
sales2 += 2.4 * i + 9.3 * j, "dollars_collected"
sales2 += 5 * i + 18 * j <= 420, "time"
sales2.writeLP("DirectMarketing.lp")
sales2.solve()
print(pulp.LpStatus[sales2.status])
for y in sales2.variables():
    print(y.name, "=", y.varValue)
print('Total_commission: $' + str(pulp.value(sales2.objective)))

sales3 = pulp.LpProblem("Direct_Marketing",pulp.LpMaximize)
i = pulp.LpVariable("phone",0,None,pulp.LpInteger)
j = pulp.LpVariable("direct",0,None,pulp.LpInteger)
sales3 += 3.36 * i + 9.3 * j, "dollars collected"
sales3+= 8 * i + 18 * j <= 420, "time"
sales3.writeLP("DirectMarketing.lp")
sales3.solve()
print(pulp.LpStatus[sales3.status])
for z in sales3.variables():
    print(x.name, "=", z.varValue)
print('Total_commission: $' + str(pulp.value(sales3.objective)))

#### Expected output#####
#### 
Optimal
direct = 23.0
phone = 0.0
Totalcommission:$213.9
Optimal
direct = 23.0
phone = 1.0
Total_commission: $216.3
Optimal
phone = 22.0
phone = 3.0
Total_commission: $214.68000000000004
####