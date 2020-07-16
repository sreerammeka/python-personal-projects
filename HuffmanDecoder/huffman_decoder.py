# Huffman Decoder
# Still need to check which solution works

# Solution 1
def decodeHuff1(root , s):
   #Enter Your Code Here
    temp=root
    string=[]
    for i in s:
        c=int(i)
        if c==1:
            temp=temp.right
        elif c==0:
            temp=temp.left
        if temp.right==None and temp.left==None:
            string.append(temp.data)
            temp=root
    b=''.join(string)
    print b

# Solution 2

def is_last(node):
    return not node.left and not node.right


def go_right(node):
    return node.right


def go_left(node):
    return node.left

    # Enter your code here. Read input from STDIN. Print output to STDOUT


def decodeHuff2(root, s):
    result = []
    node = root
    for char in s:
        if char == '1':
            node = go_right(node)
        elif char == '0':
            node = go_left(node)

        if is_last(node):
            result.append(node.data)
            node = root

    print
    ''.join(result)

# Solution 3
def decodeHuff3(root, s):

s=list(s[::-1])
t = root
while s:
    if t.right == None and t.left == None:
        print(t.data , end="")
        t = root

    if s[-1] == '0':
        t = t.left
        s.pop()
    else :
        t =t.right
        s.pop()
print(t.data)

# Solution 4
letters = {}
def decodeHuff(root, s):
    dfs(root,'')
    p = 0
    word = ''
    for i in range(1,len(s)+1):
        if s[p:i] in letters:
            word += letters[s[p:i]]
            p = i
    print(word)

def dfs(node,path):
    if node.right is None and node.left is None:
        letters[path] = node.data
    if node.right is not None:
        dfs(node.right,path+'1')
    if node.left is not None:
        dfs(node.left,path+'0')

# Solution 5
def decodeHuff(root, s):
    output = []

    def decoder(node, i):
        if i < len(s):
            if s[i] == '1':
                node = node.right
            else:
                node = node.left

            if node.data != '\0':
                output.append(node.data)
                return decoder(root, i+1)
            else:
                return decoder(node, i+1)
        else:
            return

    decoder(root, 0)

    print(''.join(output))

# Solution 6
    l=len(s)
    i=0
    st=""
    while(i<l):
        t=root
        while(t.left!=None and t.right!=None):
            if(s[i]=="1"):
                t=t.right
            if(s[i]=="0"):
                t=t.left
            i+=1
        st=st+t.data
    print(st)

# Solution 7
def decodeHuff(root, s):
    if not s or not root:
        return []

    decoded = []
    LEFT, RIGHT = "0", "1"
    is_leaf = lambda n: \
        n.left is None and n.right is None

    curr = root
    directions = list(s)
    for step in directions:
        # If curr is None
        if curr is None:
            curr = root

        # Travel the tree in the direction
        if curr.left and step is LEFT:
            curr = curr.left
        elif curr.right and step is RIGHT:
            curr = curr.right
        else:
            curr = root

        # If we arrived at a leaf
        if is_leaf(curr):
            decoded.append(curr.data)
            curr = root

    print("".join(decoded))

# Solution 8

# def decode(codes, encoded):
#     code = []
#     node = codes
#     for idx in range(encoded):
#         if node.left and encoded[idx] == '0':
#             code = str(code + node.data)
#             node = node.left
#         if node.right and encoded[idx] == '1':
#             code = str(code + node.data)
#             node = node.right
#         if node.left == None and node.right == None:
#             code = str(code + node.data)
#             node = codes
#     print(code)

# decode(110, 1101)
codes = ('a 100100', 'b 100101', '/n 111111')

def decode(codes, encoded):
    code = ''
    node = codes
    for idx in range(encoded)):
        if node.left and encoded[idx] == '0':
            code = str(code + node.data)
            node = node.left
        if node.right and encoded[idx] == '1':
            code = str(code + node.data)
            node = node.right
        if node.left == None and node.right == None:
            code = str(code + node.data)
            node = codes
    print(code)

# decode(codes, 100100111111100101110001100000)