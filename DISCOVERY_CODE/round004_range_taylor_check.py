from fractions import Fraction as F
import json
cases=[]
for s in [F(1,2),F(1),F(3,2),F(2),F(3),F(4)]:
 for n in [2,3,17]:
  p=s+2;alpha=2/p;c=2*s*p/n
  second=F(n,4)*alpha*(alpha-1)*c*c
  third=F(n,4)*alpha*(alpha-1)*(alpha-2)*c*c*c
  assert second==-2*s**3/n
  assert third==4*s**4*(2*s+2)/n**2
  original=4*s**3*(2*s+2)/n**2
  cases.append({'s':str(s),'N':n,'third_at_r1':str(third),'original_constant_valid_at_zero':original>=third})
print(json.dumps({'status':'PASS corrected third-derivative identity','arithmetic':'exact Fraction binomial coefficients; no seed or tolerance','cases':cases,'case_count':len(cases),'limitation':'root self-check; does not certify the annular stochastic argument'},indent=2))
