height = 1.75  # m
weight = 80.5  # kg

bmi = weight / height ** 2

# bmi <= 18.5 -> under fit
if bmi <= 18.5:
    print('under fit')

# 18.5 < bmi <= 25 -> normal
elif bmi > 18.5 and bmi <= 25:
    print('normal')

# 25 < bmi <= 28 -> over fit
elif bmi > 25 and bmi <= 28:
    print('over fit')

# 28 < bmi <= 32 -> fat
elif bmi > 28 and bmi <= 32:
    print('fat')

# > 32 -> over fat
elif bmi > 32:
    print('over fat')
