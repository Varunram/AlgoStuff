n = gets.to_i ; str = gets.scan(/B+/)
puts str.size
if(str[0])
  puts str.map(&:size)* ' '
end
