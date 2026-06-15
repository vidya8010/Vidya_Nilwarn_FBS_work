area_o_w=float(input('Enter area of one wall:'))
c_interiar=float(input('Enter cost of interiar wall:'))
c_exteriar=float(input('Enter cost of exteriar wall:'))

total_c=8*c_interiar*area_o_w + 7*c_exteriar*area_o_w

print(f'total cost:{total_c}')