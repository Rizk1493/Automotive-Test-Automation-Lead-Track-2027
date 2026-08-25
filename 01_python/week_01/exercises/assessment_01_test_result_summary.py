passed_tests = 0
failed_tests = 0

while True:
    test_result = input("Enter test result (pass/fail) or 'end' to finish: ").strip().lower()

    if test_result == "end":
        break
    elif test_result == "pass":
        passed_tests += 1
    elif test_result == "fail":
        failed_tests += 1
    else:
        print("Invalid input. Please enter 'pass', 'fail', or 'end'.")

total_tests = passed_tests + failed_tests

if total_tests == 0:
    pass_rate = 0
else:
    pass_rate = (passed_tests / total_tests) * 100

print(f"Passed: {passed_tests}")
print(f"Failed: {failed_tests}")
print(f"Total: {total_tests}")
print(f"Pass Rate: {pass_rate:.2f}%")
