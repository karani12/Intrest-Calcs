## Construction-Inclined Financial Functions

This is a collection of Python functions designed to be used in the construction industry for financial calculations related to investment, financing, and payment. These functions are useful for estimating the costs of a construction project, analyzing the financial viability of an investment, and calculating the payments required for loans and mortgages

`calculate_npv(cash_flows, discount_rate)`

This function calculates the net present value (NPV) of a series of cash flows given a discount rate. The cash flows should be provided as a list of tuples, where each tuple contains the amount and the year of the cash flow. The discount rate should be provided as a decimal number.

`calculate_sinking_fund_payment(present_value, interest_rate, num_periods)`
This function calculates the fixed periodic payment required to accumulate a given future value over a given number of periods at a given interest rate. This is useful for estimating the amount of money that needs to be set aside each month or year to cover future expenses or investments.

`calculate_parry_evaluation_table(interest_rate, num_periods)`
This function calculates the Parry evaluation table for a given interest rate and number of periods. The Parry evaluation table is a useful tool for determining the present value of a series of equal periodic payments.

`calculate_present_value(future_value, interest_rate, num_periods)`
This function calculates the present value of a future payment given a discount rate and the number of periods. This is useful for calculating the present value of a single future payment, such as the value of a bond or other fixed-income security.

`calculate_years_purchase(annual_income, interest_rate, num_years)`
This function calculates the years purchase of an asset given its annual income, interest rate, and number of years. The years purchase is a useful metric for determining the value of an income-producing asset.

`calculate_dual_rate(nominal_rate, inflation_rate)`
This function calculates the dual rate for a given nominal interest rate and inflation rate. The dual rate is a useful tool for comparing the real (inflation-adjusted) return of an investment to its nominal return.

`calculate_mortgage_payment(principal, interest_rate, num_periods)`

This function calculates the fixed monthly mortgage payment required to pay off a given principal over a given number of periods at a given interest rate. This is useful for calculating the monthly payment required to repay a mortgage loan.

> More functionality coming soon! This is a work in progress.It is meant to be used in conjunction with the [Construction-Inclined Financial Functions] for finacial appraisals and analysis. 



