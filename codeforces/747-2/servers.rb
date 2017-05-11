n, q = gets.split(" ").map(&:to_i)
ti = ki = di = time = available = Array.new
for i in 0..q-1
  di[i], ki[i], ti[i] = gets.split(" ").map(&:to_i)
end
print ti
loo = ti.max
for i in 0..n-1
  time[i] = 1
end
for i in 0..loo
  print "cnt="
  sum=0
  cnt = 0
  for k in 0..n-1
    if time[k]>0
      time[k] = time[k]-1
    end
    if time[k]==0
      available[k]= 1
      cnt = cnt + 1
    end
  end
  print i+1
  if i+1 == ti[i]
    print "Hoorah"
    if ((ki[i]>n) || (ki[i]>cnt))
      puts -1
    else
      for j in 0..n-1
        if available[j]==1
          available[j]=0
          sum = sum+j+1
        end
      end
      puts sum
    end
  end
end
