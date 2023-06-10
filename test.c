heapify (將一個list轉為heap)
heappush/heappop/heappushpop (放入/取出/先放入後取出)
nlargest/nsmallest (取前n大/前n小的元素)
C++
//基本輸入
//宣告為迭代器的變數 輸出需加*號
//迭代器就是指標的概念 //用在vector
include<vector>
vector.push_back(val)
vector.pop_back(val)
vector.size()    //陣列長度
vector.front()  //陣列第一個值
vector.back()  //陣列最後一個值
vector.insert(vector.begin()+i, val) //任意位置插入
vector.begin()  //陣列的頭
vector.end()     //陣列的尾
.find(first,last,val)  //就只會給val值 //宣告為迭代器
vector<int> val  //ㄧ維陣列
vector<vector<int>> val  //二維陣列
vector<int>::iterator Val=~  //算是用來指vector陣列的指標，星號取值 //迭代器的宣告在這行就要完成

include<iterator>
.distance(first,last)  //陣列長度  //宣告為迭代器
.distance(vector.begin(),val）//index值 //宣告為迭代器

include<algorithm>
.sort(fist,last,cmp)  //由小到大排序，比較函式需自訂
.reverse(first,last)   //陣列反轉
min_element(first,last)  //陣列最小值 //宣告為迭代器
max_element(first,last)  //陣列最大值 //宣告為迭代器

include<map>

include<list>

include<stack>
stack<int> name  //宣告
stack.push(val)    //頂端加入新元素
stack.pop()   //頂端移出新元素 //堆疊不能為空  空則會讓程式崩潰
stack.size()   //取得堆疊中元素數量
stack.empty() //判斷堆疊是否為空 //布林值
stack.top()    //查看最頂端的元素 //堆疊若為空會出錯
stack1.swap(stack2)  //堆疊1⃣️和堆疊2⃣️的值交換

include<queue>
queue<int> name  //宣告
queue.push(val)    //尾部加入新元素
queue.pop()   //頭部移出新元素 
queue.size()   //取得佇列中元素數量
queue.empty() //判斷佇列是否為空 //布林值
queue.front()   //查看最前面的元素queue1.swap(queue2)  //佇列1⃣️和佇列2⃣️的值交換

include<sstream>
stringstream strname //整數字串的轉換
strname.str(“”) //用完要寫
strname.clear()
