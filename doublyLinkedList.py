class Node:
	def __init__(self, data):
		self.key = data
		self.previous = None
		self.next = None
		return

	def has_value(self, value):
		if self.key == value:
			return true
		else:
			return false

class DoublyLinkedList(self, head, tail, myList):
	
	def __init__(self):
		self.head = None
		self.tail = None
		return

	def list_length(self):
		count = 0
		current_node = self.head

		while current_node is not None:
			count += 1
			current_node = current_node.next

		return count

	def output_list(self):
		current_node = self.head

		while current_node is not None:
			print(current_node.data)
			current_node = current_node.next

		return

	def unordered_search(self, value):
		current_node = self.head

		node_id = 1
		result = []

		while current_node is not None:
			re




if __name__ == '__main__':
	
