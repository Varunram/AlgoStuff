i = j = 0; list = Array.new; newlist = Array.new
while(i<4)
  list[i] = gets
  i += 1
end
while(j<4)
  newlist[j] = list[j][0] + list[j][1] + list[j][2] + list[j][3]
  j += 1
end

for i in 0..3
  if(list[i].include?("xx.") || list[i].include?("x.x") || list[i].include?(".xx") || newlist[i].include?("xx.") || newlist[i].include?("x.x") || newlist[i].include?(".xx"))
    list
    puts "YES"
    j = 1000
    break
  end
end
if (j != 1000)
  puts "NO"
end
