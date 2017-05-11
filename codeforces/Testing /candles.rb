n = gets.to_i ; i=0; a = Array.new
while(i<=n)
  a.insert(a.length,i) ;n -=i;i +=1
end
a[-1]+=n ;
puts a.length-1
for i in 1..a.length
  print a[i], " "
end
