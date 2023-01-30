john_credit = 31
john_ci = 120
john_applied_math = True
john_academic_math = False

john_met_criteria = john_credit >= 30 and john_ci >= 40 and (john_academic_math or john_applied_math)

print(f"John has met graduate criteria. This is {john_met_criteria}.")