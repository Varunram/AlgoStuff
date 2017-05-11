require 'prime'
n = gets.to_i
if n%2 == 0
  if n == 2
    print 1
  else
    print 2
  end
else
  a = Prime.prime?(n)
  b = Prime.prime?(n-2)
  if(a)
    print 1
  else
    if(b)
      print 2
      exit
    end
    print 3
  end
end
