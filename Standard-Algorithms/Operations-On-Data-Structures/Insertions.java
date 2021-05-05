//Java


//Strings
String str = "String";
str += " Insertion";

//Integers
int num = 100;
num = Integer.toString(num);
num += "0";
num = Integer.parseInt(num);

//Arrays
int[] numArr = new int[5];
for (int i = 0; i < numArr.length; i++){
  numArr[i] = i;
}

//Lists (ArrayLists)
ArrayList<Integer> numArrList = new ArrayList<Integer>(10);
for (int i = 0; i < numArrList.size(); i++){
  numArrList.add(i, i*i);
}

//2-D Arrays (Regular and Jagged)
int[][] num2dArr = new int[5][5];
//int[][] num2dArr = new int[5][10];
for (int i = 0; i < num2dArr.length; i++){
  for (int j = 0; j < num2dArr[i].length; j++){
    num2dArr[i][j] = j;
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
  
  static insertion(n, val){
    ListNode current = head;
    int count = 0;
    if (count == n){
      head = new ListNode(val);
      return;
    }
    while (count+1 < n){
      current = current.next;
    }
    ListNode in = new ListNode(val);
    ListNode next = current.next;
    current.next = in;
    in.next = tempNext;
    return head;
  }
}
      
  
  //Doubly-Linked Lists
  class ListNode(){
    int val;
    ListNode prev;
    ListNode next;
    ListNode (int x){
      val = x;
      prev = null;
      next = null;
    }
    ListNode head;
    
    static insertion(n, val){
      ListNode current = head;
      int count = 0;
      if (count == n){
        head = new ListNode(val);
        return;
      }
      while (count+1 < n){
        current = current.next;
      }
      ListNode in = new ListNode(val);
      Listnode next = current.next;
      in.prev = current;
      in.next = next;
      current.next.prev = in;
      current.next = prev;
    }
  }
    
  //Circular-Linked Lists
      class ListNode(){
        int val;
        ListNode next;
        ListNode (int x){
          val = x;
          next = null;
        }
        ListNode tail;
        static int getLength(){
          ListNode current = tail;
          if (tail == null){
            return 0;
          }
          int counter = 0;
          while (current.next != tail){
            counter++;
            current = current.next;
          }
          return counter+1;
        }
        
        static insertion(n, val){
          if (tail == null){
            tail = new ListNode(val);
            tail.next = tail;
            return;
          }
          ListNode current = tail.next;
          ListNode inserted = new ListNode(val);
          int counter = 0;
          if(n > getLength()-1){
            inserted.next = tail.next;
            tail.next = inserted;
            tail = inserted;
            return;
          }
          
          while (current.next != tail && counter + 1 < n){
            current = current.next;
            counter++;
          }
          inserted.next = current.next;
          current.next = inserted;
        }
      }
  
  //Doubly-Circular-Linked Lists
        class ListNode{
          int val;
          ListNode prev;
          ListNode next;
          ListNode (int x){
            val = x;
            prev = null;
            next = null;
          }
          ListNode tail;
          
          static insertion(n, val){
             if (tail == null){
              tail = new ListNode(val);
              tail.prev = tail;
              tail.next = tail;
              return;
            }
            ListNode current = tail.next;
            ListNode inserted = new ListNode(val);
            int counter = 0;
            if(n > getLength()-1){
              inserted.prev = tail;
              inserted.next = tail.next;
              tail.next.prev = inserted;
              tail.next = inserted;
              tail = inserted;
              return;
            }
          
            while (current.next != tail && counter + 1 < n){
              current = current.next;
              counter++;
           }
            inserted.prev = current;
            inserted.next = current.next;
            current.next.prev = inserted;
            current.next = inserted;
            
          }
        }
  
  //Stacks
  
  //Queues + Priority Queues
  
  //Trees + Binary Trees
  
  //Heaps
  
  //Sets
  
  //Maps
            
  //Graphs
