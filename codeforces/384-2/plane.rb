n,a,b = gets.chomp.split(" ").map(&:to_i)
s = gets.split("")
puts s[a-1] == s[b-1] ? 0 : 1
