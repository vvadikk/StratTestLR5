#Вариант 19
import pandas

tr_mcc_codes = pandas.read_csv('data/tr_mcc_codes.csv', sep=';')
tr_types = pandas.read_csv('data/tr_types.csv', sep=';')
transactions = pandas.read_csv('data/transactions.csv', sep=',', nrows=1000000)
transactions['tr_datetime'] = pandas.to_datetime(transactions['tr_datetime'].str.split().str[1], format='%H:%M:%S')
gender_train = pandas.read_csv('data/gender_train.csv', sep=',')
gender_train['gender'] = gender_train['gender'].map({1: 'M'}).fillna('F') #замена 1 на М и отсутствующих значений на F
new_transactions = transactions.merge(tr_mcc_codes, on='mcc_code', how='inner') \
                     .merge(tr_types, on='tr_type', how='inner') \
                     .merge(gender_train, on='customer_id', how='left')
negative_amounts = new_transactions['amount'] < 0
new_transactions.loc[negative_amounts, 'amount_bucket'] = pandas.qcut(new_transactions.loc[negative_amounts, 'amount'], q=5, labels=['Very Low', 'Low', 'Middle', 'High', 'Very High'])
new_transactions['amount_bucket'] = new_transactions['amount_bucket'].astype('category').cat.add_categories('Income')
new_transactions['amount_bucket'] = new_transactions['amount_bucket'].fillna('Income')
new_transactions['hour'] = new_transactions['tr_datetime'].dt.hour

if __name__ == '__main__':
    print(new_transactions.head())