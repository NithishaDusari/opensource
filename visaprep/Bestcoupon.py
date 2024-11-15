X=int(input())
discount1=0.1*X
discount2=100
max_discount=max(discount1, discount2)
amount_to_pay=X-max_discount
print(int(amount_to_pay))
