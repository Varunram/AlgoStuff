require 'prime'
n= gets.to_i

for i in 1..1000
  if !(Prime.prime?((i*n) + 1))
    print i
    break
  end
end
