n =gets.to_i ; list = gets.chomp.split(" ").map(&:to_i).uniq.sort
puts (list.length <= 2 || (list.length <=3 && (2*list[1] == list[0] + list[2])))? "YES" : "NO"
