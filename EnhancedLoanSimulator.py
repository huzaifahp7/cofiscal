# Loan Modification Simulator
class EnhancedLoanSimulator:
    
    def __init__(self):
        self.loans = []
        
    def add_loan(self, principal, interest_rate, term_years):
        """Adding a loan to the simulator."""
        self.loans.append({
            "principal": principal,
            "interest_rate": interest_rate,
            "term_years": term_years
        })
        
    def modify_loan(self, index, principal=None, interest_rate=None, term_years=None):
        """Modifying an existing loan."""
        if principal:
            self.loans[index]['principal'] = principal
        if interest_rate:
            self.loans[index]['interest_rate'] = interest_rate
        if term_years:
            self.loans[index]['term_years'] = term_years
            
    def calculate_payments(self):
        """Calculating monthly payments for all loans."""
        return [monthly_payment(loan['principal'], loan['interest_rate'], loan['term_years']) for loan in self.loans]
    
    def total_payments(self):
        """Calculating total payments for all loans."""
        return [monthly_payment(loan['principal'], loan['interest_rate'], loan['term_years']) * 12 * loan['term_years'] for loan in self.loans]
    
    def total_interests(self):
        """Calculating total interest for all loans."""
        return [total_interest(loan['principal'], loan['interest_rate'], loan['term_years']) for loan in self.loans]
    
    def interest_savings(self):
        """Calculating interest savings if the suggested strategy is followed."""
        _, interest_snowball, interest_avalanche = best_strategy(self.loans)
        if len(self.loans) <= 1:
            return 0
        return abs(interest_snowball - interest_avalanche)
    
    def detailed_breakdown(self, index):
        """Providing a detailed breakdown for a specific loan."""
        loan = self.loans[index]
        monthly_pay = monthly_payment(loan['principal'], loan['interest_rate'], loan['term_years'])
        total_pay = monthly_pay * 12 * loan['term_years']
        total_int = total_interest(loan['principal'], loan['interest_rate'], loan['term_years'])
        
        return {
            "monthly_payment": monthly_pay,
            "total_payment": total_pay,
            "total_interest": total_int
        }
    
    def suggest_strategy(self):
        """Suggesting a payment strategy based on total interest."""
        strategy, _, _ = best_strategy(self.loans)
        return strategy

# Functions to support the simulator
def monthly_payment(principal, interest_rate, term_years):
    r = interest_rate / 12 / 100
    n = term_years * 12
    payment = (principal*r*(1+r)**n) / ((1+r)**n - 1)
    return payment

def total_interest(principal, interest_rate, term_years):
    total_payment = monthly_payment(principal, interest_rate, term_years) * term_years * 12
    interest = total_payment - principal
    return interest

def best_strategy(loans):
    loans_snowball = sorted(loans, key=lambda x: x['principal'])
    loans_avalanche = sorted(loans, key=lambda x: x['interest_rate'], reverse=True)
    total_interest_snowball = sum([total_interest(loan['principal'], loan['interest_rate'], loan['term_years']) for loan in loans_snowball])
    total_interest_avalanche = sum([total_interest(loan['principal'], loan['interest_rate'], loan['term_years']) for loan in loans_avalanche])
    
    if total_interest_snowball < total_interest_avalanche:
        return 'Snowball', total_interest_snowball, total_interest_avalanche
    else:
        return 'Avalanche', total_interest_snowball, total_interest_avalanche