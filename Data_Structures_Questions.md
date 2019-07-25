<style TYPE="text/css">
    code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [['$','$'], ['\\(','\\)']],
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
        }
    });
    MathJax.Hub.Queue(function() {
        var all = MathJax.Hub.getAllJax(), i;
        for(i = 0; i < all.length; i += 1) {
            all[i].SourceElement().parentNode.className += ' has-jax';
        }
    });
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML-full"></script>

Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

What is the runtime complexity of `enqueue`?

$$O(1)$$
The node that is linked is a constant time process, since this is not an array, the rest of the array does not need to be reallocated with each enqueue.

What is the runtime complexity of `dequeue`?
$$O(1)$$
Same as the enqueue. The removal of the first node does not induce reallocation of any of the other elements.

What is the runtime complexity of `len`?
$$O(1)$$
It is tracked by only mathematical operations which execute in constant time.

## Binary Search Tree

What is the runtime complexity of `insert`?
Worst case scenario is:
$$O(n)$$
unless its balanced, if its balanced it would be:
$$O(lg(n))$$

What is the runtime complexity of `contains`?
Worst case scenario is:
$$O(n)$$
unless its balanced, if its balanced it would be:
$$O(lg(n))$$

What is the runtime complexity of `get_max`?
Worst case scenario is:
$$O(n)$$
unless its balanced, if its balanced it would be:
$$O(lg(n))$$

## Heap

What is the runtime complexity of `_bubble_up`?
$$O(lg(n))$$
What is the runtime complexity of `_sift_down`?
$$O(lg(n))$$
What is the runtime complexity of `insert`?
$$O(lg(n))$$
What is the runtime complexity of `delete`?
$$O(lg(n))$$
What is the runtime complexity of `get_max`?
$$O(1)$$

## Doubly Linked List

What is the runtime complexity of `ListNode.insert_after`?
$$O(1)$$
What is the runtime complexity of `ListNode.insert_before`?
$$O(1)$$
What is the runtime complexity of `ListNode.delete`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.add_to_head`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.move_to_front`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.move_to_end`?
$$O(1)$$
What is the runtime complexity of `DoublyLinkedList.delete`?
$$O(1)$$
Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
The delete method of the linked list is
$$O(1)$$
it does not have to worry about reallocation of all the other values in its structure.
Worst case for Array.splice should be
$$O(n)$$

It has to reallocate and copy every other item over one space in memory.
