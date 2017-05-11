n, k = gets.chomp.split(" ").map(&:to_i)
ans = 1;(ans +=1; k/=2;) while(k%2==0);
p ans
