import math
from scipy import stats
from scipy.stats import norm
from scipy.stats import t
from scipy.stats import f

def one_sample_t_test (data, target, tail) :
    n=len(data)
    mean=stats.tmean(data)
    std=stats.tstd(data)
    print(f"Mean Estimation: {mean}")
    if tail == 't' :
        CI1=t.ppf(0.025,n-1,mean,std/math.sqrt(n))
        CI2=t.ppf(1-0.025,n-1,mean,std/math.sqrt(n))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Mean is not equal to {target}")
        p=t.cdf(target,n-1,mean,std/math.sqrt(n))
        p=2*min(p,1-p)
        print(f"p value: {p}")
    if tail == 'g' :
        CI1=t.ppf(0.05,n-1,mean,std/math.sqrt(n))
        CI2='Infinity'
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Mean is greater than {target}")
        p=t.cdf(target,n-1,mean,std/math.sqrt(n))
        print(f"p value: {p}")
    if tail == 'l' :
        CI1='-Infinity'
        CI2=t.ppf(1-0.05,n-1,mean,std/math.sqrt(n))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Mean is less than {target}")
        p=1-t.cdf(target,n-1,mean,std/math.sqrt(n))
        print(f"p value: {p}")


def paired_t_test (data1, data2, tail) :
    data=[]
    for i in range(len(data1)) :
        data.append(data1[i]-data2[i])
    n=len(data)
    mean=stats.tmean(data)
    std=stats.tstd(data)
    print(f"Difference Estimation: {mean}")
    if tail == 't' :
        CI1=t.ppf(0.025,n-1,mean,std/math.sqrt(n))
        CI2=t.ppf(1-0.025,n-1,mean,std/math.sqrt(n))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is different from Data2")
        p=t.cdf(0,n-1,mean,std/math.sqrt(n))
        p=2*min(p,1-p)
        print(f"p value: {p}")
    if tail == 'g' :
        CI1=t.ppf(0.05,n-1,mean,std/math.sqrt(n))
        CI2='Infinity'
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is greater than Data2")
        p=t.cdf(0,n-1,mean,std/math.sqrt(n))
        print(f"p value: {p}")
    if tail == 'l' :
        CI1='-Infinity'
        CI2=t.ppf(1-0.05,n-1,mean,std/math.sqrt(n))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is less than Data2")
        p=1-t.cdf(0,n-1,mean,std/math.sqrt(n))
        print(f"p value: {p}")


def two_sample_t_test (data1, data2, tail) :
    n1=len(data1)
    m1=stats.tmean(data1)
    s1=stats.tstd(data1)
    n2=len(data2)
    m2=stats.tmean(data2)
    s2=stats.tstd(data2)
    mean=m1-m2
    std=math.sqrt( ( (n1-1)*pow(s1,2)+(n2-1)*pow(s2,2) ) / (n1+n2-2) )
    print(f"Difference Estimation: {mean}")
    if tail == 't' :
        CI1=t.ppf(0.025,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        CI2=t.ppf(1-0.025,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is different from Data2")
        p=t.cdf(0,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        p=2*min(p,1-p)
        print(f"p value: {p}")
    if tail == 'g' :
        CI1=t.ppf(0.05,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        CI2='Infinity'
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is greater than Data2")
        p=t.cdf(0,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        print(f"p value: {p}")
    if tail == 'l' :
        CI1='-Infinity'
        CI2=t.ppf(1-0.05,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        print(f"95% Confidence interval: {CI1} ~ {CI2}")
        print(f"Hypothesis: Data1 is less than Data2")
        p=1-t.cdf(0,n1+n2-2,mean,std*math.sqrt(1/n1+1/n2))
        print(f"p value: {p}")

def anova (data) :
    x=0
    n=0
    k=len(data)
    for i in data :
        x+=sum(i)
        n+=len(i)
    x/=n
    Sb=0
    Sw=0
    for i in data :
        Sb+=len(i)*pow(stats.tmean(i)-x,2)
        Sw+=(len(i)-1)*pow(stats.tstd(i),2)
    Sb/=(k-1)
    Sw/=(n-k)
    p=1-f.cdf(Sb/Sw,k-1,n-k)
    print(f"Hypothesis: There is difference between the {k} groups")
    print(f"p value: {p}")


# Example of one sample t test
# bp=[5,7,8,13,16,19]
# one_sample_t_test(bp,0,'t')

# Example of paired t test
# u1=[150,155,153,162,160,170]
# u2=[145,148,145,149,144,151]
# paired_t_test(u1,u2,'g')

# Example of two sample t test
# A=[3,7,1,15,9,13,15,13,13,10]
# B=[1,2,11,6,8,3,0,1,2,1,4]
# two_sample_t_test(A,B,'t')

# Example of anova
# g=[]
# g1=[8.55,8.48,6.38,9.27,7.97,6.85]
# g2=[7.4,8.63,8.53,5.36,9.2]
# g3=[5.99,6.75,7.28,5.72,8.73,6.29]
# g4=[7.02,5.23,6.15,6.78,6.61,7.36,4.95,6.33]
# g.append(g1)
# g.append(g2)
# g.append(g3)
# g.append(g4)
# anova(g)
