# Jade Tan, Jarrett Singian, Martin Tierro

def solve(e,t):
    return compute_exponent(e, t)


def compute_exponent(base, power):
    MOD = int(1e7)
    if power == 0:
        return 1
    else:
        sub_power = power // 2
        half_power_mod = compute_exponent(base, sub_power) % MOD
        temp_value = (half_power_mod * half_power_mod) % MOD
        if power%2 == 1:
            temp_value = (temp_value * base) % MOD
        return temp_value

  
e, t = list(map(int,input().rstrip().split(" ")))
print(solve(e,t))