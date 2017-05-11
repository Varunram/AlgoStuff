n, k =gets.chomp.split(" ").map(&:to_i)
string=Array.new
for i in 0..n-1
  string[i]=gets.chomp
end
n = gets.chomp
string = string.sort_by(&:size).select{ |x| x.size <= n.size }
if string[0].size == n.size
  print 1
else
  ctr = string.select{|x| x.size<n.size}.size
  print ctr+(ctr/k)*5 + 1
end
print " "
print string.size + ((string.size-1)/k)*5
