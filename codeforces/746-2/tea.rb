n, k, a, b = gets.chomp.split(" ").map(&:to_i)
s = ''
if a<=b
  ctr = 1
else
  ctr = -1
end
a1 = [a,b].min # a1 = b
b1 = [a,b].max #
if b1 > k*(a1+1)
  print "NO"
else
  while(b1 - a1 > k)
    if (ctr == 1)
      s = s + "B"*k + "G"
    else
      s = s + "G"*k + "B"
    end
    b1-=k
    a1-=1
  end
  if ctr == 1
    s += "B"*(b1-a1)
    s += "GB"*a1
  else
    s += "G"*(b1-a1)
    s +="BG"*a1
  end
  puts s
end
