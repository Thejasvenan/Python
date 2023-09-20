class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)

    #####################################################################
    ######### Your task is to implement the following methods. ##########
    #####################################################################
    
    def insert(self, data, bracketed):
        '''
        Insert operators and operands into the binary tree.

        :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', ‘+’)
        :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
        we set bracketed as True.
        :return: self
        '''
        #Include your code here
        
        # If data is Operand
        if data[0]=="OPERAND":
            if self.left is None:
                # storing in left child
                self.left = Node(data)
            elif self.right is None:
                # storing in right child
                self.right = Node(data)
            elif self.right.right is None:
                # inserting in right child of right child
                self.right.insert(data, False)
                
        # If data is Operator
        elif data[0]=="OPERATOR":
            # for non bracket data
            if not bracketed:
                Brack_no = self
                self = Node(data)
                # self reassignment is carried down
                self.left = Brack_no
            else: # for bracketed data
                Brack_in = Node(data)
                Brack_in.insert(self.right.data, False) 
                # self reassignment is carried down
                self.right = Brack_in
        return self   
                
    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''
        #Include your code here
        
        # If there is no left and right child
        if self.left is None and self.right is None:
            # Return the data value in self
            return self.data[1]
        else:
            # If the Operator is "^"
            if self.data[1] == "^":
                # Changing it to "**" and concatanate strings as the operands and operators
                Total = str(self.left.evaluate()) + "**" + str(self.right.evaluate())
            else:
                # Concatanate strings as the operands and operators 
                Total = str(self.left.evaluate()) + self.data[1] + str(self.right.evaluate())
            # Changing the Total into Integer for calculating the value as in the code as string by using eval()
            value = int(eval(Total))
        # returning the evaluated value
        return value
