n = gets.to_i
if n%2 == 0
  print n/2, "\n", "2 "*(n/2)
else
  print n/2, "\n", "2 "*(n/2-1), "3"
end
