def main()
   CHAR_MIN = -2**7
   CHAR_MAX = 2**7 - 1

   val = int(input())

   num_list = list(map(int, str(abs(val))))
   num_list.reverse()
   rev_val = int(''.join(map(str,num_list)))
   if val < 0:
      rev_val *= -1

   if rev_val < CHAR_MIN or CHAR_MAX < rev_val:
       print("no solution")
   else:
       print(rev_val)
         

if __name__=='__main__':
   main()
