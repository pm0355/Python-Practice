def monthlypayment(principal, period, rate):
    nperiod = 0 - int(period)
    mpayment =((float(rate)/12)/(1-(1+(float(rate)/12))**(int(nperiod))))*long(principal)
    return mpayment
def loancost(principal, months, mpayment):
    cost = int(months) * float(mpayment) - long(principal)
    return long(cost)

def main():
    monies = raw_input(" Enter principal: ")
    time = raw_input(" Enter months: ")
    intrst = raw_input(" Enter yearly interest rate: ")
    monthlypayment(monies, time, intrst)
    loancost(monies, time, intrst)
    paymentx = monthlypayment(monies, time, intrst)
    costy = loancost(monies, time, paymentx)
               
    print "The cost of the loan will be: $" + str(long(costy))
main()
               
            
               
