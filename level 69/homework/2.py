def split_by_a():
    sentence = input("enter a sentence: ")
    fragments = sentence.split("a")
    for idx, fragment in enumerate(fragments):
        print(f"ნაწილი {idx +1}: {fragments}")

split_by_a()
