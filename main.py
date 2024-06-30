from model.page import Page
from model.block import Block
import logging

from stack_model.my_stack import Stack

from heap_model.my_heap import MinHeap

from queue_model.my_queue import Queue


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def run_node_example():
    logging.info("Running node example...")

    page1 = Page(id="page1")
    print(page1)

    # 创建一个块并添加到页面中
    block1 = Block(id="block1", content="This is a block")
    page1.add_child(block1)
    print(page1.children)

    # 创建一个嵌套的页面并添加到块中
    nested_page = Page(id="nested_page")
    block1.add_child(nested_page)
    print(block1.children)

    # 创建一个块并添加到嵌套页面中
    nested_block = Block(id="nested_block", content="This is a nested block")
    nested_page.add_child(nested_block)
    print(nested_page.children)

def run_stack_example():
    logging.info("Running stack example...")
    # Last in First Out
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
    print("栈的大小:", stack.size())  # 输出: 栈的大小: 3

    print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
    print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 2
    print("栈的大小:", stack.size())  # 输出: 栈的大小: 2

    stack.pop()
    stack.pop()
    print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: True

def run_heap_example():
    logging.info("Running heap example...")
    min_heap = MinHeap()

    min_heap.push(5)
    min_heap.push(3)
    min_heap.push(8)
    min_heap.push(10)
    min_heap.push(1)
    min_heap.push(-1)

    print("堆顶元素:", min_heap.peek())  # 输出: 堆顶元素: 1
    print("堆的大小:", min_heap.size())  # 输出: 堆的大小: 4

    print("弹出元素:", min_heap.pop())  # 输出: 弹出元素: 1
    print("堆顶元素:", min_heap.peek())  # 输出: 堆顶元素: 3
    print("堆的大小:", min_heap.size())  # 输出: 堆的大小: 3

    while not min_heap.is_empty():
        print("弹出元素:", min_heap.pop())

    print("堆是否为空:", min_heap.is_empty())  # 输出: 堆是否为空: True

def run_queue_example():
    logging.info("Running queue example...")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("队列的大小:", queue.size())  # 输出: 队列的大小: 3

    print("弹出元素:", queue.dequeue())  # 输出: 弹出元素: 1

if __name__ == "__main__":
    run_node_example()
    run_stack_example()
    run_heap_example()
    run_queue_example()