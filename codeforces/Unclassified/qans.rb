n = gets.to_i
h = Hash.new(0)
n.times do |i|
  x, num = gets.split(" ")
  a =  num.tr('0-9', '0101010101').to_i
  if x.ord == 43
    h[a] += 1
  elsif x.ord == 45
    h[a] -= 1
  elsif x.ord == 63
    puts h[a]
  end
end
