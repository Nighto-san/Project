def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0: return ''
    res = ''
    for i in range(len(strarr)):
        comb_str = ''.join(strarr[i:i+k])
        if len(comb_str) > len(res):
            res = comb_str
    return res








print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck",sep='\n')
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta",sep='\n')
print()
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh",sep='\n')
print()
print(longest_consec([], 3), "")