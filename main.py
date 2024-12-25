result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Number 'a' less than 'b'")
        if b > 100:
            raise IndexError("Value of 'b' exceed 100")
        return a / b
    except Exception as e:
        print(f"Error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, (1,): 15, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Steam processing error ({key}, {value}): {e}")

print(result)