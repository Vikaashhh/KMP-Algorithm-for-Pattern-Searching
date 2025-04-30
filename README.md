# 🔍 Day 18 of #gfg160 – Pattern Searching using KMP Algorithm 
## 🧠 Problem Statement:
Given a pattern pat and a text txt, efficiently find all the starting indices where the pattern occurs in the text.

## 🔗 Why KMP?
The naive approach rechecks characters unnecessarily.
💡 KMP avoids this by precomputing an LPS (Longest Prefix Suffix) array to know how much to skip, ensuring linear time complexity.

## Strategy:
1. Step 1: LPS array banao — tells us how far to "rollback" on a mismatch.

2. Step 2: Traverse txt aur pat simultaneously:

- Agar match mila, aage badho.

- Agar mismatch hua, rollback karo using LPS instead of starting from scratch.

## 📈 Time & Space Complexity:
Time: O(N + M)

Space: O(M) for the LPS array

## 🧠 Learning Outcome:
✅ You’ve now unlocked one of the most optimized solutions for substring searching. KMP is the foundation for efficient pattern recognition, crucial in compilers, DNA matching, and search engines.

## 📌 Hashtags:
#Day18 #gfg160 #geekstreak2025 #kmpalgorithm #stringmatching #pythondeveloper #dsa #techlearning #interviewprep #dsawithvikash #dsawithpython

