n, k = gets.chomp.split(" ").map(&:to_i)
start = Array.new; end1 = Array.new; maximum = Array.new; minimum = Array.new; i1 = Array.new; j1 = Array.new; ctr = Array.new;
for i in 0..n-1
  start[i], end1[i] = gets.chomp.split(" ").map(&:to_i)
end
for i in 0..n-1
  for j in i+1..n-1
    maximum[j]=[start[i], start[j]].max
    minimum[j]=[end1[i], end1[j]].min
    if (maximum[j]<minimum[j])
      ctr[i] = minimum[j] - maximum[j] + 1
      i1[i] = i
      j1[i] = j
    end
  end
end

max = 0
for x in 0..n-1
  if ctr[x] == nil
    ctr[x] = -1
  end
end
sum = 0
for i in 0..k-2
  sum += ctr.sort.reverse[i]
end
if sum > 0
  puts sum
  for i in 0..k-2
    for j in 0..n-1
      if ctr[j] == ctr.sort.reverse[i]
        break
      end
    end
    print i1[j]+1 , " ", j1[j]+1
  end
else
  puts 0
  print "1 2"
end
=begin
  1 100
120 130
125 180
 40 70
=end
