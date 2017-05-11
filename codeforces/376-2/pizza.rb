n = gets.to_i
a = gets.split(" ").map(&:to_i)
ans = 0
a.each do |e|
  break if (e <ans)
  ans = (e - ans)%2
end
print ans>0? "NO" : "YES"
