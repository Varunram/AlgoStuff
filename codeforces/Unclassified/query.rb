n = gets.to_i
i = ctr = flag = 0
arr = Array.new
while(i< 12)
  puts "i= ",  i
  op, num = gets.chomp.split(" ")
  puts "op= ", op, "num = ", num, "\n"
  if op.ord == 43
    if i == 0
      arr.insert(-1, num)
      puts "SHITTY LANGUAGE"
      puts arr
    else
    arr.insert(arr.length, num)
  end
  elsif op.ord == 45
    arr.slice!(arr.find_index(num))
  else
    ctr =0
    arr.each do |i|
      if i.length < num.length
        cmpi = "0"*(num.length-i.length) + i
        cmpnum = num
      elsif (i.length > num.length)
        cmpnum = "0"*(i.length-num.length) + num
        cmpi = i
      else
        cmpi = i
        cmpnum = num
      end
      cmpnum = cmpnum.split("")
      cmpi = cmpi.split("")
      for i in 0..num.length - 1
        cmpi[i] = cmpi[i].to_i + cmpnum[i].to_i
        if (cmpi[i]%2 != 0)
          flag = 1
          break
        end
      end
      if flag == 0
        ctr +=1
      end
    end
    puts ctr
  end
  i += 1
  puts arr
end
