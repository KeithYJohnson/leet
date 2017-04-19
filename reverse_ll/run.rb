require 'pry-byebug'
class Node
  attr_accessor :val, :next

  def initialize(val)
    self.val = val
  end

  def reverse
    array = []
    current = self

    while current
      array << current
      current = current.next
    end

    (array.length - 1).downto(0) do |i|
      current_node = array[i]
      next_node    = array[i - 1]
      current_node.next = next_node
    end

    array[0].next = nil

    array[array.length - 1]
  end

  def fast_reverse
    return self unless next_node = self.next

    current     = self
    placeholder = next_node.next

    unless placeholder
      self.next      = nil
      next_node.next = self
      return next_node
    end

    self.next = nil
    while placeholder

      next_node.next = current
      current        = next_node
      next_node      = placeholder

      if placeholder.next
        placeholder = placeholder.next
      else
        next_node.next = current
        break
      end
    end

    return next_node
  end
end

root        = Node.new(1)
second      = Node.new(2)
root.next   = second
third       = Node.new(3)
second.next = third
fourth      = Node.new(4)
third.next  = fourth

current = root.fast_reverse
while current
  puts current.val
  current = current.next
end



new_root = Node.new(5)
result = new_root.reverse
p result.val == 5


new_root.next = Node.new(6)
result = new_root.reverse
p result.val == 6
p result.next.val == 5
