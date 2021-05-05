//Java

//Strings
String str = "String";
for (int i = 0; i < str.length(); i++){
  //Insert Code
}

//Integers
int num = 123;
while (num != 0){
  int selected = num % 10;
  num = num/10;
}

//Arrays
int[] numArr = {1, 2, 3, 4}
for (int i : numArr){
  //Insert Code
}
for (int i = 0; i < numArr.length; i++){
  //Insert Code
}

//Lists (ArrayLists)
ArrayList<Integer> numArrList = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4));
for (Integer i : numArrayList){
  //Insert Code
}
for (int i = 0; i < numArrList.size(); i++){
  //Insert Code
}

//2-D Arrays (Regular and Jagged)
int[][] num2dArr = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
for (int[] i : num2dArr){
  for (int j : i){
    //Insert Code
  }
}
for (int i = 0; i < num2dArr.length; i++){
  for (int j = 0; j < num2dArr[i].length; j++){
    //Insert Code
  }
}

//Singly-Linked Lists
//1 -> 2 -> 3 -> 4 -> NULL
class ListNode(){
  int val;
  ListNode next;
  ListNode (int x){
    val = x;
    next = null;
  }
  ListNode head;
  ListNode current = head;
  while(current != null){
    current = current.next;
  }
  
  //Doubly-Linked Lists
  
  //Circular-Linked Lists
  
  //Doubly-Circular-Linked Lists
  
  //Stacks
  
  //Queues + Priority Queues
  
  //Trees + Binary Trees
  
  //Heaps
  
  //Sets
  
  //Maps
  
  
