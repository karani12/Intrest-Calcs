def calculate_npv(cash_flows, discount_rate):
    """
    Calculates the net present value (NPV) of a list of cash flows using a given discount rate.
    """
    npvs = [] # initialize list to store NPVs
    for cf in cash_flows:
        amount, year = cf
        discount_factor = 1 / (1 + discount_rate) ** year # calculate discount factor
        pv = amount * discount_factor # calculate present value
        npvs.append(pv) # append present value to list of NPVs
    return npvs


def calculate_parry_table(discount_rate, num_years):
    """
    Calculates Parry's Evaluation Table for a given discount rate and number of years.
    """
    parry_table = [] # initialize list to store Parry's Evaluation Table
    for year in range(1, num_years+1):
        discount_factor = 1 / (1 + discount_rate) ** year # calculate discount factor
        factor_times_years = discount_factor * year # multiply discount factor by number of years
        parry_table.append(factor_times_years) # append result to Parry's Evaluation Table
    return parry_table


def calculate_sinking_fund(amount, interest_rate, num_years):
    """
    Calculates the sinking fund factor (i.e., the periodic payment required to accumulate a given amount in a given number of years).
    """
    sinking_fund_factor = (interest_rate * amount) / (1 - (1 + interest_rate) ** -num_years) # calculate sinking fund factor
    return sinking_fund_factor

def calculate_years_purchase(annual_income, interest_rate, num_years):
    """
    Calculates the years purchase of an asset given its annual income, interest rate, and number of years.
    """
    years_purchase = (1 - (1 + interest_rate) ** -num_years) / interest_rate # calculate years purchase factor
    value = annual_income * years_purchase # calculate value of asset
    return value

def calculate_dual_rate(nominal_rate, inflation_rate):
    """
    Calculates the dual rate for a given nominal interest rate and inflation rate.
    """
    dual_rate = ((1 + nominal_rate) / (1 + inflation_rate)) - 1 # calculate dual rate
    return dual_rate

def calculate_annuity(present_value, interest_rate, num_periods):
    """
    Calculates the annuity payment required to pay off a given present value over a given number of periods at a given interest rate.
    """
    annuity = (interest_rate * present_value) / (1 - (1 + interest_rate) ** -num_periods) # calculate annuity payment
    return annuity

def calculate_mortgage_payment(principal, interest_rate, num_periods):
    """
    Calculates the fixed monthly mortgage payment required to pay off a given principal over a given number of periods at a given interest rate.
    """
    monthly_interest_rate = interest_rate / 12 # calculate monthly interest rate
    num_payments = num_periods * 12 # calculate total number of payments
    mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments) # calculate mortgage payment
    return mortgage_payment
