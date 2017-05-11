=begin
#include<iostream>
#include<algorithm>
#include<string>
using namespace std; using std::cin; using std::cout;

int main(){
  long long int x, sum, n, flag; char a[10000]; sum =flag=0;
  cin>>n;
  for (int i=0;i<n;i++){
    cin>>x;
    cin>>a;
    if (a[0]=='S'){
      sum += x;
    } else if (a[0] == 'N'){
      sum -= x;
    } else {
      if ((sum==0) || (sum == 20000)){
        flag = 0;
      }
    }
    if((sum < 0) || (sum > 20000))
    { flag = 0;cout<<"NO";}
  }
  flag = sum == 0? 1 : 0;
  if (flag == 0)
  cout<<"NO";
  else
  cout<<"YES";
}
=end
s= 0
gets.to_i.times{
  x, y = gets.chomp.split(" ")
  if y == 'North'
    s -= x.to_i
  elsif y == 'South'
    s += x.to_i
  else
    if s==0 || s==20000
      puts :NO
      exit
    end
    next
  end
  if s<0 || s> 20000
    puts :NO
    exit
  end
}
puts s==0? :YES : :NO
