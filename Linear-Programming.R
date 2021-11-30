library(lpSolveAPI)
train < -data.frame(wagon=c('w1','w2','w3'), weightcapacity=c(10,8,12), spacecapacity=c(5000,4000,8000))
cargo <- data.frame(type=c('c1','c2','c3','c4'), available=c(18,10,5,20), volume=c(400,300,200,500),profit=c(2000,2500,5000,3500))
lpmodel<-make.lp(2*NROW(train)+NROW(cargo),12)
column<-0
row<-0
for(wg in train\$wagon){
    	row<-row+1
    	for(type in seq(1,NROW(cargo\$type))){
    	column <- column+
	    set.column(lpmodel,column,c(1, cargo[type,'volume'],1), indices=c(row,NROW(train)+row, NROW(train)*2+type))}}
set.constr.value(lpmodel, rhs=train$weightcapacity, constraints=seq(1,NROW(train)))
set.constr.value(lpmodel, rhs=train$spacecapacity, constraints=seq(NROW(train)+ 1,NROW(train)*2))
set.constr.value(lpmodel, rhs=cargo$available, constraints=seq(NROW(train)*2+1, NROW(train)*2+NROW(cargo)))
set.objfn(lpmodel, rep(cargo$profit,NROW(train)))
lp.control(lpmodel,sense='max')
solve(lpmodel)
get.objective(lpmodel)