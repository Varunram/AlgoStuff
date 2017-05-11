n, m = gets.chomp.split(" ").map(&:to_i)
x = 1000000000
for i in 0..m-1
  li, ri = gets.chomp.split(" ").map(&:to_i)
  x = [ri - li+1, x].min
end
puts x
for i in 0..n-1
  print (i%x), " "
end
