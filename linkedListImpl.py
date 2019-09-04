class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

	def __str__(self):
		return "\nNode: Value- "+ str(self.value) + "\nNext Node- {" + str(self.next) + "}\n"
'''
	def traverseLinkedList(self):
		node = self
		while node != None:
			print node.value
			node = node.next


if __name__ == "__main__":
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(12)
	n4 = Node(16) 

	n1.next = n2
	n2.next = n3
	n3.next = n4

	n1.traverseLinkedList()
'''