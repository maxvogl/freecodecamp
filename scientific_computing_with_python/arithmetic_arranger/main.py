# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# print("Example task")
# print("Addition example:    485 + 158")
# print("Subtraction example: 485 - 158")
# task = str(input("Enter your mathematical addition (+) or subtraction (-) task:"))
# solution = input("Press Enter to check solution!")
# print(arithmetic_arranger([task], True))

# Run unit tests automatically
main(module='test_module', exit=False)
