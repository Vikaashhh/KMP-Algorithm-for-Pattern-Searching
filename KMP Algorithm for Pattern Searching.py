#User function Template for python3

class Solution:
    def search(self, pat, txt):
        
        # LPS (Longest Prefix which is also Suffix) banane wali function
        def createLPS(p):
            lps = [0] * len(p)
            length = 0  # previous longest prefix-suffix
            i = 1

            while i < len(p):
                if p[i] == p[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    # agar mismatch hua aur length != 0, toh peeche jao
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = createLPS(pat)  # pattern ke liye LPS array bana liya
        res = []
        i = 0  # txt pointer
        j = 0  # pat pointer

        # jab tak pura text traverse nahi kar lete
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1

            if j == len(pat):
                # match mil gaya
                res.append(i - j)
                j = lps[j - 1]  # next possible match ke liye shift karo

            elif i < len(txt) and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j - 1]  # mismatch hua toh pattern ke pointer ko shift karo
                else:
                    i += 1  # agar j = 0 hai toh sirf text pointer badhao

        return res


# Example Execution:
if __name__ == "__main__":
    ob = Solution()
    txt = "geeksforgeeks"
    pat = "geek"
    result = ob.search(pat, txt)
    print(result)  # Output: [0, 8]