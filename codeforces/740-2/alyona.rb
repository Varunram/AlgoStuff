n,a,b,c = gets.chomp.split(" ").map(&:to_i)
puts n%4 == 0? 0 : n%4==3? [a,b+c,3*c].min : (n%4==2? [2*a,b,2*c].min : (n%4==1? [3*a,a+b,c].min : -1))
