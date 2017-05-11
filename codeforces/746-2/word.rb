n = gets.to_i
str = gets.chomp
res = Array.new
if n%2 != 0
  k = i =1
  ctr =1
  res[n/2] = str[0]
  while(k <= n/2)
      if (i == 1)
        res[n/2-k] = str[ctr]
        i = -1
      else
        res[n/2+k] = str[ctr]
        i=1
      end
      ctr +=1
      if(ctr%2 != 0)
        k = k+1
      end
  end
else
  k=1
  i=1
  ctr = 0
  while(k <= n/2)
      if (i == 1)
        res[n/2-k] = str[ctr]
        i = -1
      else
        res[n/2+k-1] = str[ctr]
        i=1
      end
      ctr +=1
      if(ctr%2 == 0)
        k = k+1
      end
  end
end

print res.join("")
