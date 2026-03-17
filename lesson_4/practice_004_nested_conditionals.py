

test_score = int(input("Enter your test score (0-100): "))


if test_score > 0:                          # Outer if
    if test_score > 90:                     # Inner if #1
        print("Excellent!")
    elif test_score >= 70 and test_score <= 90:  # Inner elif
        print("Good job!")
    else:                                   # Inner else (covers 1–69)
        print("Keep working hard!")
else:                                       # Outer else (covers ≤ 0)
    print("No test score available")