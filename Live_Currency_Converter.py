import streamlit as st
import requests

st.title('Live Currency Converter')
### API URL
url = f'https://api.exchangerate-api.com/v4/latest/INR'
response = requests.get(url)
data = response.json()
currency_list = list(data['rates'].keys())

### Currency Selection
select_currency = st.selectbox('Select currency to convert to:', currency_list,key='currency_select')
amount = st.number_input(f'Enter amount in {select_currency}:', min_value=1)
target_curr = st.selectbox('Select currency to convert to:',currency_list,key='target_currency_select')


if st.button('Convert'):
    url = f'https://api.exchangerate-api.com/v4/latest/INR'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_curr]
        if select_currency != 'INR':
            rate_inr = data['rates'][select_currency]
            converted_amount_inr = amount / rate_inr
            converted_amount = converted_amount_inr * rate
        else:
            converted_amount = amount * rate
        st.success(f'{amount} {select_currency} is equal to {converted_amount:.2f} {target_curr}')
    else:
        st.error('Failed to fetch exchange rates.')