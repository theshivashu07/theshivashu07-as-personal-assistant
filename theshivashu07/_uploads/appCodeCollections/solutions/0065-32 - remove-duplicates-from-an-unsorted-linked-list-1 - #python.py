

#User function Template for python3
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        checkerdict=dict()
        primehead=tracknode=Node(None)
        while(head!=None):
            isrepeted=checkerdict.get(head.data)==None
            if(isrepeted and (head.next==None or head.data!=head.next.data)):
                checkerdict[head.data]=True
                tracknode.next=head
                tracknode=tracknode.next
            head=head.next
        # for safty purpose, we assume...
        tracknode.next=None  
        return primehead.next

