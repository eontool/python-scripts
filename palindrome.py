#Reverse any given integer
def reverse(n):

  x=0
  
  while(n!=0):
    x=x*10+n%10
    n=n/10
  return x

#Check if any given integer is a palindrome
def palindrome(n):
	if (n/reverse(n)!=1):
		return False
	else:
		return True

print palindrome(123404321)
