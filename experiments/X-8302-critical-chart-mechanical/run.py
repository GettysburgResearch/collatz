#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from decimal import Decimal
from pathlib import Path
from arithmetic import exact_order_2, quotient_rows
from intervals import fixed_interval_chart, fixed_interval_pr45
from mechanical import (
    A, ACH, CHART_FLOOR, CHART_MASK_HI, CHART_MASK_LO, CHART_POSITIONS,
    EXCESS, FACTORS, K, MODULUS, NCH, P_HI, P_LO, PR45_FLOOR,
    PR45_POSITIONS, Q_HI, Q_LO, chart_delta, chart_letter,
    disjoint_sites, identity, mechanical_product,
)
def lower_word(p,q):return [((j+1)*p)//q-(j*p)//q for j in range(q)]
def direct_constant(vals):
    C=0;E=0
    for a in vals:C=3*C+(1<<E);E+=a
    return C
def farey_checks(limit=36):
    count=0
    for q in range(2,limit+1):
      for p in range(1,q):
       if math.gcd(p,q)>1:continue
       for s in range(2,limit+1):
        for r in range(1,s):
         if math.gcd(r,s)>1 or p*s>=r*q or r*q-p*s!=1:continue
         L=lower_word(p,q);R=lower_word(r,s);w=L+R;v=R+L
         assert w==lower_word(p+r,q+s)
         dif=[i for i,(a,b) in enumerate(zip(w,v)) if a!=b]
         assert dif==[s-1,s] and w[s-1:s+1]==[0,1] and v[s-1:s+1]==[1,0]
         assert direct_constant([1+b for b in w])-direct_constant([1+b for b in v])==-(1<<(r+s-1))*3**(q-1)
         count+=1
    return count
def generate():
    assert K%2==0 and ACH==2*K-A and 4*NCH-ACH==A
    assert P_HI*Q_LO-P_LO*Q_HI==1 and 4*Q_LO+Q_HI==K and 4*P_LO+P_HI==EXCESS
    farey_count=farey_checks();orders=[exact_order_2(p) for p in FACTORS];cover=math.lcm(*orders);assert cover>EXCESS
    pr_rows,pr_q,pr_floor,pr_ceil=quotient_rows('accel',PR45_POSITIONS,PR45_FLOOR);pr_iv=fixed_interval_pr45();assert int(pr_iv.lo)==int(pr_iv.hi)==PR45_FLOOR and pr_q not in (pr_floor,pr_ceil)
    sites=disjoint_sites(ACH,NCH,80);mask=CHART_MASK_LO+(CHART_MASK_HI<<64);idxs=[i for i in range(80) if mask>>i&1]
    assert len(idxs)==41 and tuple(sites[i][0] for i in idxs)==CHART_POSITIONS
    baseM=mechanical_product(ACH,NCH,False,chart_letter(0,MODULUS),chart_letter(1,MODULUS),identity(MODULUS),lambda x,y:x*y).constant
    modM=(baseM+sum(chart_delta(sites[i],MODULUS) for i in idxs))%MODULUS;assert modM==0
    ch_iv=fixed_interval_chart(idxs);assert int(ch_iv.lo)==int(ch_iv.hi)==CHART_FLOOR
    ch_rows,ch_q,ch_floor,ch_ceil=quotient_rows('chart',CHART_POSITIONS,CHART_FLOOR);assert ch_q not in (ch_floor,ch_ceil)
    nearest=min(ch_iv.lo-Decimal(CHART_FLOOR),Decimal(CHART_FLOOR+1)-ch_iv.hi)
    return {'schema_version':1,'experiment_id':'X-8302','farey_mechanical_commutator':{'small_neighbor_pairs_checked':farey_count,'critical_lower':[P_LO,Q_LO],'critical_upper':[P_HI,Q_HI],'determinant':1,'target_decomposition':'4*lower + 1*upper','commutator_abs_power_2':P_HI+Q_HI-1,'commutator_abs_power_3':Q_LO-1},'order_cover':{'factors':list(FACTORS),'orders':orders,'lcm':cover,'excess_window':EXCESS,'covers_word':True},'pr45_quotient_cylinder':{'rows':pr_rows,'crt_modulus':MODULUS,'crt_quotient_residue':pr_q,'fixed_point_lower':str(pr_iv.lo),'fixed_point_upper':str(pr_iv.hi),'unique_floor':PR45_FLOOR,'floor_mod_M':pr_floor,'ceil_mod_M':pr_ceil,'modular_nonintegrality':True},'negative_three_chart':{'chart_blocks':NCH,'expanding_blocks':ACH,'accelerated_length':K,'total_valuation':A,'same_denominator_as_pr45':True,'base_numerator_mod_M':baseM,'swap_mask_hi':CHART_MASK_HI,'swap_mask_lo':CHART_MASK_LO,'selected_swap_count':len(idxs),'selected_positions':list(CHART_POSITIONS),'modified_numerator_mod_M':modM,'fixed_point_lower':str(ch_iv.lo),'fixed_point_upper':str(ch_iv.hi),'interval_width':str(ch_iv.hi-ch_iv.lo),'unique_floor':CHART_FLOOR,'distance_to_nearest_integer_lower_bound':str(nearest),'quotient_rows':ch_rows,'crt_modulus':MODULUS,'crt_quotient_residue':ch_q,'floor_mod_M':ch_floor,'ceil_mod_M':ch_ceil,'modular_nonintegrality':True,'conclusion':'the frozen paired-chart word is not an integral cycle'},'boundaries':{'proved':['Farey-neighbor monomial commutator','five-factor order cover','p-adic quotient-cylinder residues','paired-chart proper-factor divisibility','directed real and modular rejection of both frozen words'],'not_proved':['complete denominator factorization','a positive nontrivial cycle','an infinite two-branch chart path','a Collatz counterexample']}}
def canonical_bytes(p):return (json.dumps(p,sort_keys=True,indent=2)+'\n').encode()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-results',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args();data=canonical_bytes(generate());digest=hashlib.sha256(data).hexdigest()
    if a.write_results:a.write_results.parent.mkdir(parents=True,exist_ok=True);a.write_results.write_bytes(data)
    if a.check_results and a.check_results.read_bytes()!=data:raise SystemExit('canonical mismatch')
    print(data.decode(),end='');print('SHA256',digest)
if __name__=='__main__':main()
