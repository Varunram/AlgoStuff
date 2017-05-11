string = gets.to_s.chomp; sum =0 ;string.insert(0,"a")
for i in 0..string.length-2
    a = string[i+1].ord - string[i].ord
    a = a >13? 26-a : a<0? a<-13? 26+a : -a : a
    sum += a
end
puts sum
