a2 = gets.to_i
str = gets.to_s
count_a = count_g = count_c = count_t = 0
for i in 0..a2-1
  e = str[i]
  a = e.ord
  if (a==65)
    count_a = count_a + 1
  end
  if (a==67)
    count_c = count_c + 1
  end
  if (a==71)
    count_g = count_g + 1
  end
  if (a==84)
    count_t = count_t + 1
  end
end
count_q = a2 - (count_a + count_c + count_g + count_t)
no = a2 / 4

if (a2%4 !=0)||(count_a > no) || (count_c > no) || (count_g > no) || (count_t > no) || ((count_a + count_c + count_g + count_t) > a2)
  print("===")
  flag = 1
elsif count_q == 0
  print str
  flag = 1
end

if (flag != 1)
  count_a = -count_a + no
  count_g = -count_g + no
  count_c = -count_c + no
  count_t = -count_t + no

  stack = Array.new
  for i in 1..count_a
    stack.push("A")
  end
  for i in 1..count_g
    stack.push("G")
  end
  for i in 1..count_c
    stack.push("C")
  end
  for i in 1..count_t
    stack.push("T")
  end
  k =0
  for i in 0..a2-1
    a= str[i].ord
    if (a==63)
      str[i]=stack[k]
      k = k+1
    end
  end
  puts str
end
