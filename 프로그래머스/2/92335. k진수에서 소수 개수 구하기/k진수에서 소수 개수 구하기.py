def solution(n, k):
    n2k = make_k(n, k)
    # pn = prime_numbers(10000)
    # n2k_list = [x for x in str(n2k).split('0') if x!='' and int(x) in pn]
    n2k_list = [x for x in str(n2k).split('0') if x!='' and is_prime(int(x))]
    return len(n2k_list)

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
# # n 이하의 소수 리스트
# def prime_numbers(n):
#     is_prime = [True]*(n+1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(n**0.5) +1):
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False
#     primes = [i for i in range(2, n+1) if is_prime[i]]
#     return primes

# k진수 변환
def make_k(num, k):
    temp = ''
    while num:
        digit = num%k
        if digit<10:
            temp+= str(digit)
        else:
            temp+= chr(digit-10+'A')
        num//=k
    return temp[::-1]