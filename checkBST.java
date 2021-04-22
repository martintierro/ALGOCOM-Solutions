/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
//SINGIAN, JARRETT ETHAN        TAN, JADE NICOLE    TIERRO, MARTIN ANGELO
boolean checkBST(Node root) {
    return checkBSTDown(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        
}

boolean checkBSTDown (Node root, int min, int max){
    if (root == null)
        return true;
    
    else if (root.data<min||root.data>max)
        return false;
    
    return checkBSTDown(root.left, min, root.data-1)&&checkBSTDown(root.right,root.data+1,max);
    
}