import sys
sys.path.insert(0,'.')
def A(n): return n//2 if n%2==0 else (3*n+1)//2
def merging(k):
    X=9*k+1; Y=27*k+2; p=2; q=3
    while True:
        if X==Y and p==q: return True
        if X in (1,2) and Y in (1,2): return False
        if X&1: X=(3*X+1)//2; p+=1
        else: X//=2
        if Y&1: Y=(3*Y+1)//2; q+=1
        else: Y//=2
# Lemma 5.1 in accelerated form, all odd z>=3 incl. small ones
bad=0;cnt=0
for z in range(3,200001,2):
    m=z+1;b=0
    while m%2==0: m//=2;b+=1
    if m%4==(1 if b%2==0 else 3):
        cnt+=1
        x=z;y=z-1
        for _ in range(b+2): x=A(x);y=A(y)
        if not (x==y==(3**b*m-1)//4): bad+=1
print("Lemma 5.1 accelerated form: cases",cnt,"failures",bad)
# chain of powers of 3:  link I(n): 3^n => 6*3^n+1  is C(3^(n-1));  link II(n): 6*3^n+1 => 3^(n+1) is C(2*3^(n-1))
J=int(sys.argv[1])
I=[];II=[]
for n in range(1,J+1):
    I.append(merging(3**(n-1))); II.append(merging(2*3**(n-1)))
for cut in [10,20,50,100,200,400,J]:
    if cut<=J:
        a=sum(I[:cut]);b=sum(II[:cut]);both=sum(1 for t in range(cut) if I[t] and II[t])
        print(f"n<= {cut:4d}: links 3^n=>6*3^n+1 merging: {a}/{cut}   links 6*3^n+1=>3^(n+1) merging: {b}/{cut}   both (so P(3^n)<=>P(3^(n+1)) proved): {both}/{cut}")
print("first n with link I merging:",[n+1 for n in range(J) if I[n]][:15])
print("first n with link II merging:",[n+1 for n in range(J) if II[n]][:15])
