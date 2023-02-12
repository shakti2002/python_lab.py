
def isPalindrome(str):
 
  
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "madam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("given string is not a palindron")