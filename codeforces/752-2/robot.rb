require 'set'
n = gets.chomp
s = gets.chomp
rev = {"U" => "D", "D" => "U", "L" => "R", "R" => "L"}
otp = 0
set = Set.new
s.each_char do |i|
  x = i
  if(set.include?(rev[x])) || ((set.size() == 2)&& !(set.include?(x)))
    otp +=1
    set.clear
  end
  set.add(x)
end
if(set.size>0)
  otp +=1
end
puts otp
