import linkedListImpl

class Node(linkedListImpl.Node):
	def traverseLinkedList(self):
		node = self
		while node != None:
			print node.value
			node = node.next

	def removeDuplicates(self):
		listWithoutDuplicates = []
		node = self
		previous = None

		while node != None:
			if node.value in listWithoutDuplicates:
				previous.next = node.next
			else:
				listWithoutDuplicates.append(node.value)
			previous = node
			node = node.next

		for val in listWithoutDuplicates:
			print(val)

	def kToLast(self, k):
		if k < 0:
			return None

		iter_1 = self
		#print(iter_1)
		iter_2 = self
		i = -1
		a = []
		while iter_1 != None:
			iter_1 = iter_1.next
			#print(iter_1)
			#print(iter_1.value)
			if i < k:
				i += 1
			else:
				if iter_2 != None:
					a.append(iter_2.value)
				iter_2 = iter_2.next
		for val in a:
			print(a)
		
		if i == k:
			return iter_2.value
		else:
			return None


if __name__ == "__main__":
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(12)
	n4 = Node(16) 
	n5 = Node(12)
	n6 = Node(5)

	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6

	#n1.traverseLinkedList()
	#n1.removeDuplicates()

	n1.kToLast(5)

