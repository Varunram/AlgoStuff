l1, r1 , l2, r2, k = gets.chomp.split(" ").map(&:to_i)
start = [l1,l2].max
end1 = [r1,r2].min
if ((end1-start)>=0)
  if k.between?(start, end1)
    print end1-start
  else
    print end1-start+1
  end
else
  print 0
end
