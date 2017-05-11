n, m =gets.chomp.split(" ").map(&:to_i)
list = Array.new; list2 = Array.new
ctr =0
for i in 0..n-1
  list[i] = gets.to_s
end
for i in 0..m-1
  list2[i] = gets.to_s
end
for i in 0..n-1
  for j in 0..m-1
    if list[i] == list2[j]
      ctr += 1
    end
  end
end
if (ctr%2 == 0)
  n, m = n-ctr/2, m-ctr/2
else
  n,m = n-ctr/2, m-ctr/2 - 1
end
puts n>m ? "YES": "NO"
