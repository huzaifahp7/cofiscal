#!pip install -U google-generativeai
import google.generativeai as palm
import re
palm.configure(api_key='AIzaSyAedmPMHxXBrjTQFgOoypvQIYZLiz6L21k')

def generate_text(income, loan_amt, credit_score, interest_rate, loan_term, dti_ratio, loan_purp, prob_def):
    print(prob_def)
    typ = {1:"Other",
           2:"Auto",
           3:"Business",
           4:"Home",
           5:"Education"}
    loan_purp = typ[loan_purp]
    out = []
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
        prompt += '''Explain to me why I am on the safer side. Mention the loan amount explicitly. Keep it as concise and specific as possible. Additionally, suggest why I should go ahead and take the loan 
        whilst giving me general financial tips. Keep it as concise and general as possible, not exceeding more than 50 words.
        Return a python list as the output.
        The first entry should be the reason why my probability of defaulting is low and why I should take the loan. 
        The second entry should be measures I can take to reduce the risk. The third
        entry should be general financial tips on taking loans and avoiding defaulting.'''
        out = palm.chat(messages = prompt)
    
    


    else:
        prompt+= '''Explain why I am at risk of defaulting. Mention the loan amount explicitly. Additionally, suggest based on current market trends and conditions, 
        what I should do to avoid defaulting. Give me genral financial tips
        such as how to prevent defaulting. For example, if you are telling me to 
        increase my income then give me general financial tips to do so. 
        Keep it as concise and general as possible, not exceeding more than 50 words. Return a python list as the output.
        The first entry should be the reason why my probability of defaulting is high. 
        The second entry should be measures I can take to reduce the risk. The third
        entry should be general financial tips on taking loans and avoiding defaulting.'''
        out = palm.chat(messages = prompt)
        
        
    


    
    text = out.last
    entries = text.split('\n\n')
    entries = [entry.strip() for entry in entries if entry.strip()]
    


    # Use regex to add newline after "{number}."
    entries = [re.sub(r'(\d+\.)', r'\n\1', entry) for entry in entries]

    return entries