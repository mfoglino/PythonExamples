

def isTherePath(matriz, i, j, s, n, m):

	result = False

	if not s:
		return True;
	

	print(i,j,s)

	result = matriz[i][j]==s[0]

	result = result and (
			(isInRange(i,j+1, n, m) and isTherePath(matriz, i, j+1, s[1:], n, m)) or
			(isInRange(i,j-1, n, m) and isTherePath(matriz, i, j-1, s[1:], n, m)) or
			(isInRange(i+1,j, n, m) and isTherePath(matriz, i+1, j, s[1:], n, m)) or
			(isInRange(i-1,j, n, m) and isTherePath(matriz, i-1, j, s[1:], n, m)) 
			)		
	return result;
	


def isInRange(i, j, n, m):		
	if i<0 or j < 0:
		return False
	if i>n or j > m:
		return False
	
	return True



def main():
	sopa = [['a','b','c','d'],['a','h','o','x'],['a','z','l','x'],['a','s','a','x']]		
	print(isTherePath(sopa, 1, 1, "hola", 4, 4))


if __name__=='__main__':
	main()

	