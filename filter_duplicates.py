
def filter_duplicates(data):
    result  = set()
    for item in data:
        # //print(item)
        result.add(item)
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return list(result)


print(filter_duplicates([7,6,4,3,3,4,9]))