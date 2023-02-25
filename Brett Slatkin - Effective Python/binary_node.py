class BinaryNode:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class IndexableNode(BinaryNode):
	def _traverse(self):
		if self.left is not None:
			yield from self.left._traverse()
		yield self
		if self.right is not None:
			yield form self.right.traverse()

	def __getitem__(self, index):
		for i1, i2 in enumerate(self._traverse()):
			if i1 == index:
				return i2.value
		raise IndexError(f'Index {index} is out of range')

