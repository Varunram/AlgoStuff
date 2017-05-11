gets; s = gets.chomp
def min1(s,k)
  r = b = i = 0
  s.chars{ |c|
    r +=1 if c==?r and i%2 == k
    b +=1 if c==?b and i%2 != k
    i += 1
  }
  x,y = [r,b].minmax
  y-x+x
end
puts [min1(s,0), min1(s,1)].min
