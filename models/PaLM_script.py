#!pip install -U google-generativeai
import google.generativeai as palm
import re
palm.configure(api_key='AIzaSyAedmPMHxXBrjTQFgOoypvQIYZLiz6L21k')

def generate_text(income, loan_amt, credit_score, interest_rate, loan_term, dti_ratio, loan_purp,prob_def):

    prompt = '''Discard all the previous instructions.
    Behave like you are a financial expert and are an expert at analyzing risks of defaulting 
    while taking a loan. Given my annual income of '''
    prompt +=income
    prompt += ''', my credit score of '''
    prompt += credit_score
    prompt += ''', the interest rate of '''
    prompt += interest_rate
    prompt += ''', my loan term of '''
    prompt += loan_term
    prompt += ''', my DTI ratio of '''
    prompt += dti_ratio
    prompt += ''' and my purpose of taking the loan which is: '''
    prompt+= loan_purp
    prompt+= '''. Explain why taking a loan of '''
    prompt+= loan_amt
    prompt+= ''' is giving me a probability of defaulting of '''
    prompt+= prob_def

    if (float(prob_def)<0.50):
        prompt += '''Explain to me why I am on the safer side 
        and why I should go ahead and take the loan.'''
    else:
        prompt+= '''Explain why I am at risk of defaulting. Additionally, suggest based on current market trends and conditions, 
        what I should do to avoid defaulting. Give me genral financial tips
        such as how to prevent defaulting. For example, if you are telling me to 
        increase my income then give me general financial tips to do so.'''
    


    res = palm.chat(messages = prompt)
    return res.last