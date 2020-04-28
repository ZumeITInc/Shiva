l1=[num**2 for num in range(1,5)]
print(l1)
l2=[num**3 for num in range(1,10)]
print(l2)
l3=[num for num in range(1,100) if num%3==0]
print(l3)
total_profit=25000
percentage_of_investment=[40,20,22,18]
amount_tobe_shared=[(total_profit*share)/100 for share in percentage_of_investment]
print(amount_tobe_shared)
share_less_than_40_percent=[(total_profit*share)/100 for share in percentage_of_investment if share<40]
print(share_less_than_40_percent)
