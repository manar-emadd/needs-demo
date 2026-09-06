with open("numbers.txt") as f:
    numbers = [int(line.strip()) for line in f]

print(f"Found {len(numbers)} numbers: {numbers}")
assert len(numbers) == 5, "Expected exactly 5 numbers!"
print("✅ Number check passed!")