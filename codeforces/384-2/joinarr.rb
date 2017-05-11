n, k = gets.chomp.split(" ").map(&:to_i)
a = Array.new
a.insert(a.length, 1)
if n>1
  for i in 2..n
    b = a
    a.insert(a.length, *b)
    a.insert((a.length+1)/2, i)
  end
  puts a[k-1]
else
  puts 1
end
