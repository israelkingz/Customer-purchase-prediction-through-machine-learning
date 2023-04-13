import streamlit as st
import numpy as np
import string
import pickle
import pandas as pd 
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('my_model_updatedLRC.pkl','rb'))

# Define the user interface
st.title('Purchase Prediction')
st.write('Enter the customer information to get the prospensity to purchase')

total_order = st.number_input('Total orders', min_value=0, max_value=10000, value=100)
avg_item_ordered = st.number_input('Average item ordered', min_value=0, max_value=100, value=5)
avg_product_weight = st.number_input('Average product weight', min_value=0, max_value=100, value=2)
average_order_value = st.number_input('Average order value', min_value=0.0, max_value=1000.0, value=50.0)
average_score = st.number_input('Average score', min_value=0.0, max_value=5.0, value=4.0)
total_order_in_review = st.number_input('Total orders in review', min_value=0, max_value=100, value=2)
delta_last_first = st.number_input('Days between first and last order', min_value=0, max_value=365, value=30)
avg_days_per_order = st.number_input('Average days per order', min_value=0, max_value=365, value=5)
rev_transaction_ratio = st.number_input('Revenue to transaction ratio', min_value=0.0, max_value=100.0, value=20.0)
number_product_purchase_category = st.number_input('Number of product categories purchased', min_value=0, max_value=10, value=2)

# Checkbox dropdown for most common day of week to buy
modus_dow_buy = st.multiselect('Most common day of week to buy', ['0', '1', '2', '3', '4', '5', '6'])

# Checkbox dropdown for most common month to buy
modus_month_buy = st.multiselect('Most common month to buy', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# Checkbox dropdown for most common part of day to buy
modus_partofday_buy = st.multiselect('Most common part of day to buy', ['Afternoon', 'Evening', 'Morning', 'Night'])

# Checkbox dropdown for preferred payment type
preferred_payment_type = st.multiselect('Preferred payment type', ['Boleto', 'Credit Card', 'Debit Card', 'Voucher'])

# Prepare the input data as a Pandas DataFrame
data = {
    'total_order': [total_order],
    'avg_item_ordered': [avg_item_ordered],
    'avg_product_weight': [avg_product_weight],
    'average_order_value': [average_order_value],
    'average_score': [average_score],
    'total_order_in_review': [total_order_in_review],
    'delta_last_first': [delta_last_first],
    'avg_days_per_order': [avg_days_per_order],
    'rev_transaction_ratio': [rev_transaction_ratio],
    'number_product_purchase_category': [number_product_purchase_category],
    'modus_dow_buy_0': [int('0' in modus_dow_buy)],
    'modus_dow_buy_1': [int('1' in modus_dow_buy)],
    'modus_dow_buy_2': [int('2' in modus_dow_buy)],
    'modus_dow_buy_3': [int('3' in modus_dow_buy)],
    'modus_dow_buy_4': [int('4' in modus_dow_buy)],
    'modus_dow_buy_5': [int('5' in modus_dow_buy)],
    'modus_dow_buy_6': [int('6' in modus_dow_buy)],
    'modus_month_buy_1': [int('1' in modus_month_buy)],
    'modus_month_buy_2': [int('2' in modus_month_buy)],
    'modus_month_buy_3': [int('3' in modus_month_buy)],
    'modus_month_buy_4': [int('4' in modus_month_buy)],
    'modus_month_buy_5': [int('5' in modus_month_buy)],
    'modus_month_buy_6': [int('6' in modus_month_buy)],
    'modus_month_buy_7': [int('7' in modus_month_buy)],
    'modus_month_buy_8': [int('8' in modus_month_buy)],
    'modus_month_buy_9': [int('9' in modus_month_buy)],
    'modus_month_buy_10': [int('10' in modus_month_buy)],
    'modus_month_buy_11': [int('11' in modus_month_buy)],
    'modus_month_buy_12': [int('12' in modus_month_buy)],
    'modus_partofday_buy_afternoon': [int('Afternoon' in modus_partofday_buy)],
    'modus_partofday_buy_evening': [int('Evening' in modus_partofday_buy)],
    'modus_partofday_buy_morning': [int('Morning' in modus_partofday_buy)],
    'modus_partofday_buy_night': [int('Night' in modus_partofday_buy)],
'preferred_payment_type_boleto': [int('Boleto' in preferred_payment_type)],
'preferred_payment_type_credit_card': [int('Credit Card' in preferred_payment_type)],
'preferred_payment_type_debit_card': [int('Debit Card' in preferred_payment_type)],
'preferred_payment_type_voucher': [int('Voucher' in preferred_payment_type)]

}
input_data = pd.DataFrame(data)

if st.button('Predict'):
    # Get the predicted churn probability for the input data using the model
    churn_prob = model.predict_proba(input_data)[:, 1]

    if churn_prob >= 1:
                   st.write('This customer is likely to buy a product.')
    else:
            st.write('This customer is not likely to buy a product.')