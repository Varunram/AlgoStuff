n = gets.to_i
x = y = 0
for i in 1..Math.sqrt(n).round
  if (n%i === 0)
    x = i
    y = n/i
  end
end
puts '%d %d' %[x, y]
