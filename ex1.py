# coding: utf-8

# Apply wirtinger calculus on complex valued
# function


def f(z):
    # (x**2 - y**2 + 2jxy) * (x - jy) = (x**2 - y**2)*x
    return z**2 * z.conjugate()


def fconj(z):
    return (z.conjugate()) ** 2 * z


def fr(z):
    # (f(z) + bar(f(z))/2
    return (f(z)).real


def fi(z):
    # (f(z) - bar(f(z))/(2j)
    return (f(z)).imag


def dfr_dz(z):
    return 0.5 * (2 * z * z.conjugate() + (z.conjugate()) ** 2)


def dfi_dz(z):
    return (2 * z * z.conjugate() - (z.conjugate()) ** 2) / (2j)


def df_dz(z):
    return 2 * z * z.conjugate()


z0 = 1 - 1j
print(fi(z0), f(z0))

Nsteps = 100000
epsilon = 0.001
for i in range(Nsteps):
    # z0 = z0 - epsilon * (dfr_dz(z0) - 1j * dfi_dz(z0))
    z0 = z0 - epsilon * (df_dz(z0)).conjugate()
    # print(z0, f(z0))
