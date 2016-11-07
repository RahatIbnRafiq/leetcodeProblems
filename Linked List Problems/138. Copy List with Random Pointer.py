def factory():
	return RandomListNode(0)

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		if not head:
			return None
		temp = head
		node_map =collections.defaultdict(factory)
		node_map[None] = None # avoid None as key to generate a RandomListNode
		while temp:
			node_map[temp].label = temp.label
			node_map[temp].next = node_map[temp.next]
			node_map[temp].random = node_map[temp.random]
			temp = temp.next
		del node_map[None]
		return node_map[head]
