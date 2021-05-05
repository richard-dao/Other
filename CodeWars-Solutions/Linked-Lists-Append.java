//Java
class Node {

  int data;
  Node next = null;

  Node(final int data) {
    this.data = data;
  }

  public Node(int data, Node next) {
    this.data = data;
    this.next = next;
  }

  public static Node append(Node listA, Node listB) {
    Node current = listA;
    if (listA == null && listB == null){
      return null;
    }
    
    if (listB == null){

    return listA;
    }
    
    if (listA == null){
      return listB;
    }
    
    while(current.next != null){
      current = current.next;
    }
    current.next = listB;
    return listA;

  }
}
