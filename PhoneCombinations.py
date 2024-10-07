def letterCombinations(digits):
    if not digits:
        return []
    
    digit_to_char = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

   
    result = [""]

   
    for digit in digits:
        temp = [] 
        for combination in result:
            for letter in digit_to_char[digit]:
                temp.append(combination + letter)
        result = temp 

    return result

# Sample inputs
inputs = ["23", "7", "92", "", "234", "79", "86"]

for input_str in inputs:
    print(f"Input: \"{input_str}\"")
    print(f"Output: {letterCombinations(input_str)}\n")
