# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xy2Dy-bAkf5fDSnTdju30_IQ8OhG0z47
"""

# Commented out IPython magic to ensure Python compatibility.
# # cheak the number is odd and even
# %%file Q1.cpp
# #include<iostream>
# using namespace std;
# bool isodd( int num){
#     if(num%2==0){
#         return false;
# 
#     }
#     else{
#         return true;
#     }
# 
# }
# int main(){
#     int a;
#     cin>>a;
#     for ( int i=1;i<=a;i++){
#         if(isodd(i)){
#             cout<<i<<" ";
#         }
#     }
# }

!g++ Q1.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# %%file Q2.cpp
# #include<iostream>
# using namespace std;
# bool isprime(int n){
#     for( int i=2;i<=(n-1);i++){
#         if(n%i==0)
#             return false;
# 
# 
#         }
#     return true;
#     }
# 
# 
# int main(){
#     int n;
#            cin>>n;
#             cout<<isprime(n);
# 
# }

!g++ Q2.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #array
# %%file Q3.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int array[]={1,7,9,4,5};
# 
# 
#    // cout<<sizeof(array)<<endl;
# int v=sizeof(array)/sizeof(array[0])
# 
# 
#     for( int i=0;i<v;i++){
#     cout<<array[i]<<endl;
#     }
# 
#     }

!g++ Q3.cpp
!./a.out



# Commented out IPython magic to ensure Python compatibility.
# #array
# %%file Q3.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int array[]={1,7,9,4,5};
# int v=sizeof(array)/sizeof(array[0]);
# for( int i=0;i<v;i++){
#     cout<<array[i]<<endl;
#     }
#     for(int ele:array){
#         cout<<ele<<endl;
#     }
# 
#     }

!g++ Q3.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # input of the aray
# %%file Q4.cpp
# #include<iostream>
# using namespace std;
# int main(){
#   char voi[5];
#   for ( int ind=0;ind<5;ind++){
#       cin>>voi[ind];
#   }
#     for ( int ind=0;ind<5;ind++){
#       cout<<voi[ind];
#   }
# }

!g++ Q4.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # find the sum of the given array
# %%file Q5.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[]={1,2,5,7,8};
#     int sum=0;
#     int v= sizeof(arr)/sizeof(arr[0]);
#     for(int i=0;i<v;i++){
#         cout<<arr[i]<<endl;
#         sum+=arr[i];
# 
# 
#     }
#      cout<<sum<<endl;
# }

!g++ Q5.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #find the max elemnet of the array
# %%file Q6.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[]={2,4,65,78,98};
#     int max=arr[0];
#     for ( int i=1;i<5;i++){
#         if ( arr[i]>max){
#             max=arr[i];
#         }
#     }
#     cout<<max<<endl;
# }

!g++ Q6.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # linear search
# %%file Q7.cpp
# # include<iostream>
# using namespace std;
# int main(){
#     int n;
#     cin>>n;
#     int arre=-1;
#     int arr[]={3,5, 6,7,9};
#     for ( int i=0;i<5;i++){
#         if(arr[i]==n){
#              arre=sizeof(arr[i]);
#         }
# 
#     }
#     cout<<arre<<endl;
# }

!g++ Q7.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # vector
# %%file Q8.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int> v;
#     cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
# 
#     v.push_back(5);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
#     v.push_back(7);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
#         v.push_back(6);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
#         v.push_back(4);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
#         v.push_back(3);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
#         v.push_back(8);
#       cout<<"size"<<v.size()<<endl;
#     cout<<"capacity"<<v.capacity()<<endl;
# }

!g++ Q8.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #for loop using int vector
# %%file Q9.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int>v;
#       int element;
#     for ( int i=0;i<6;i++){
# 
#         cin>>element;
#         v.push_back(element);
#     }
#     for( int i=0;i<v.size();i++){
#         cout<<v[i]<<" ";
#     }
#     cout<<endl;
# }

!g++ Q9.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # find the last occrance of the last vector
# %%file Q10.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int> v(5);
#      for ( int i=0;i<5;i++){
#         cin>>v[i];
# 
#      }
#     cout<<"enter the value of x is :"<<endl;
#     int x;
#     cin>>x;
#     int acco=-1;
#     for( int i=0;i<v.size();i++){
#         if(v[i]==x){
#             acco=i;
#         }
#     }
# cout<<acco<<endl;
# }

!g++ Q10.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# 
# # find the number of the sum  of occurrence
# %%file Q11.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int>v(6);
#     for( int i=0;i<6;i++){
#         cin>>v[i];
#     }
#     cout<<"enter the number of vector :"<<endl;
#     int x;
#     cin>>x;
#     int sum=0;
#     for( int i=0;i<v.size();i++){
#         if(v[i]==x){
#             sum+=1;
#         }
#     }
# cout<<sum<<endl;
# }

!g++ Q11.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # find the number of elemnet strictly greater than x .
# %%file Q12.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int> v(7);
#     for( int i=0;i<6;i++){
#         cin>>v[i];
#     }
#     cout<<"enter the value of x :"<<endl;
#     int x;
#     int sum=0;
#     cin>>x;
#     for( int i=0;i<v.size();i++){
#         if(v[i]>x){
#             sum+=1;
#         }
#     }
#     cout<<sum<<endl;
# }

!g++ Q12.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #cheak short or not
# %%file Q13.cpp
# #include<iostream>
# #include<vector>
# using namespace std;
# int main(){
#     vector<int>v(5);
#     for( int i=0;i<5;i++){
#         cin>>v[i];
# 
#     }
#     bool sorted=true;
#     for( int i=0;i<v.size();i++){
#         if(v[i]<=v[i-1]){
#           sorted=false;
#         }
#     }
#     cout<<sorted<<" -meanig of 1 is array is soted or 0 not sorted"<<endl;
# }

!g++ Q13.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # find the pari of sum
# %%file Q14.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[6];
#     for ( int i=0; i<6;i++){
#         cin>>arr[i];
#     }
#     cout<<"enter the value of x:"<<endl;
#     int x;
#     cin>>x;
#     int ans=0;
#     for(int i=0;i<6;i++){
#         for (int j=i+1;j<6;j++){
#             if(arr[i]+arr[j]==x){
#                 ans+=1;
#             }
#         }
#     }
#     cout<<ans<<endl;
# }

!g++ Q14.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #count the number of triplets sum equal to x
# %%file Q15.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[7];
#     for( int i=0;i<7;i++){
#         cin>>arr[i];
# 
#     }
#     cout<<"enter the value of target :"<<endl;
#     int x;
#     cin>>x;
# int sum=0;
#     for( int i=0;i<7;i++){
#         for( int j=i+1;j<7;j++){
#             for(int k=j+1;k<7;k++){
#                 if(arr[i]+arr[j]+arr[k]==x){
#                     sum+=1;
#                 }
#             }
#         }
#     }
#     cout<<sum<<endl;
# }

!g++ Q15.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # find the uniqe number
# %%file Q16.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[7];
#     for( int i=0;i<7;i++){
# 
#                           cin>>arr[i];
#     }
# 
#     for( int i=0;i<7;i++){
#         for( int j=i+1;j<7;j++){
#             if(arr[i]==arr[j]){
#                 arr[i]=arr[j]=-1;
#             }
#         }
#     }
#      int x=0;
#     for( int i=0;i<7;i++){
#         if(arr[i]>0){
#             cout<<arr[i]<<endl;
#         }
#     }
# 
# }

!g++ Q16.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# #find the secand largest element
# %%file Q17.cpp
# #include<iostream>
# #include<cmath>
# #include<limits.h>
# using namespace std;
# int largestelementind( int arr[],int size){
#       int max=INT_MIN;
#                                             int maxind=-1;
#        for( int i=0;i<size;i++){
#           if(arr[i]>max){
#               max=arr[i];
#               maxind=i;
#           }
#        }
# return maxind;
# 
# }
# int main(){
#     int arr[7];
#     for( int i=0;i<7;i++){
#         cin>>arr[i];
# 
#     }
#     int indexoflar=largestelementind(arr,7);
# arr[indexoflar]=-1;
#     int indexofsecandlargest=largestelementind(arr,7);
#     cout<<"the secand largest number"<<endl;
#     cout<<arr[indexofsecandlargest]<<endl;
#     return 0;
# }

!g++ Q17.cpp
!./a.out

# Commented out IPython magic to ensure Python compatibility.
# # rotate the array
# %%file Q18.cpp
# #include<iostream>
# using namespace std;
# int main(){
#     int arr[]={1,37,3,9,7};
#     int n=5;
#     int k;
#     cin>>k;
#     k=k%n;
#     int ansarr[5];
#     int j=0;
#     for(int i=n-k;i<n;i++){
#         ansarr[j++]=arr[i];
#     }
#     for( int i=0;i<=k;i++){
#         ansarr[j++]=arr[i];
#     }
#     for( int i=0;i<n;i++){
#         cout<<ansarr[i]<<" ";
#     }
# 
# }

!g++ Q18.cpp
!./a.out

