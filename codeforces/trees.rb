require 'set'
n = gets.to_i
list = [0] + gets.chomp.split(" ").map(&:to_i)
set = Set.new
for i in 1..n
  if(list[list[i]] == i)
    set.add([i,list[i]].min)
  end
end
print set.length
