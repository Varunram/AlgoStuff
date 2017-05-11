n = gets.to_i ;list = gets.chomp.split(" ").map(&:to_i)
puts n == 1? (list[0] == 15? "DOWN" : list[0] == 0? "UP" : -1) :  (list[n-1]-list[n-2] == -1)? (list[n-1] == 0? "UP": "DOWN") : (list[n-1] == 15? "DOWN" : "UP")
