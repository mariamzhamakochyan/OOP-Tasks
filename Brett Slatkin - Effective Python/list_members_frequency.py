class FrequencyList(list):
	def __init__(self, members):
		super().__init__(members)

	def frequency(self):
		count = {}
		for item in self:
			count[item] = count.get(item, 0) + 1
		return count
foo = FrequencyList(['a', 'b', 'c', 'd', 'a', 'b', 'a'])
print('List: ', foo)
print('Length is', len(foo))
foo.pop()
print('After pop: ', repr(foo))
print('Frequency: ', foo.frequency())
