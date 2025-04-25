def convert_to_words(num):
    if 0 <= num <= 19:
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return words[num]
    else:
        return "Number out of range (0-19)"


for i in range(20):
    print(f"{i} -> {convert_to_words(i)}")