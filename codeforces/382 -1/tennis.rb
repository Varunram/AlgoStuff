n = gets.to_i
a,b,i = 0,1,0
while a<=n
  a,b, = b, a+b
  i +=1
end
p i-3
