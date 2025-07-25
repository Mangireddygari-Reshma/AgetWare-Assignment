def combining_lists():
    def overlap_ratio(a, b):
        left = max(a[0], b[0])
        right = min(a[1], b[1])
        overlap = max(0, right - left)
        length_a = a[1] - a[0]
        length_b = b[1] - b[0]
        return overlap / length_a if length_a else 0, overlap / length_b if length_b else 0

    def get_input_list(label):
        lst = []
        n = int(input(f"\nHow many elements in {label}? "))
        for i in range(n):
            pos = input(f"→ {label} #{i+1} positions (start,end): ").strip()
            values = input(f"→ {label} #{i+1} values (comma-separated): ").strip()
            start, end = map(int, pos.split(','))
            val_list = list(map(int, values.split(',')))
            lst.append({"positions": [start, end], "values": val_list})
        return lst

    print(" Enter data for List 1")
    list1 = get_input_list("List 1")

    print("\n Enter data for List 2")
    list2 = get_input_list("List 2")

    combined = []
    used2 = set()
    for i, elem1 in enumerate(list1):
        merged = False
        for j, elem2 in enumerate(list2):
            if j in used2:
                continue
            ratio1, ratio2 = overlap_ratio(elem1["positions"], elem2["positions"])
            if ratio1 >= 0.5 or ratio2 >= 0.5: 
                combined_elem = {
                    "positions": [min(elem1["positions"][0], elem2["positions"][0]),
                                  max(elem1["positions"][1], elem2["positions"][1])],
                    "values": elem1["values"] + elem2["values"]
                }
                combined.append(combined_elem)
                used2.add(j)
                merged = True
                break
        if not merged:
            combined.append(elem1)

    for j, elem2 in enumerate(list2):
        if j not in used2:
            combined.append(elem2)

    combined.sort(key=lambda x: x["positions"][0])

    print("\n Final Combined Output:")
    for item in combined:
        print(item)
combining_lists()