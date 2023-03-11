def search_true_followed_by_false(n):
    # Search for a true value followed by a false value
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"READ {mid}")
        value = input().strip()
        if value == "true":
            if mid == n - 1 or input(f"READ {mid + 1}\n").strip() == "false":
                print(f"OUTPUT {mid}")
                return
            else:
                left = mid + 1
        else:
            right = mid - 1

# Read the number of test cases
t = int(input())

for i in range(t):
    # Read the length of the array
    n = int(input())

    # Search for a true value followed by a false value in the array
    search_true_followed_by_false(n)