n,m = gets.chomp.split(" ").map(&:to_i)
list = gets.chomp.split(" ").map(&:to_i)
i = n
while(i>=0)
  list[i+1] = list[i]
  i -=1
end
sum = 0
for i in 1..m
  l,r = gets.chomp.split(" ").map(&:to_i)
  for j in l..r
    sum+= list[j]
  end
end
puts sum
