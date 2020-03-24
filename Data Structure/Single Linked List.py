class node:
    """
    Linked list Node
    """

    def __init__(self, data: str = None) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} , {self.next}"


class Single_Linked_List:
    """
    Single Linked List
    """

    def __init__(self) -> None:
        self.__head = None

    def __is_empty(self) -> None:
        """
        Check if linked list is empty
        """
        if self.__head == None:
            print("Linked List Empty")
            return True
        return False

    def __add___head(self, data: str) -> None:
        new_node = node(data=data)
        self.__head = new_node

    def insert_at_front(self, data: str) -> None:
        if self.__head == None:
            self.__add___head(data=data)
            return
        new_node = node(data=data)
        new_node.next = self.__head
        self.__head = new_node

    def insert_at_end(self, data: str) -> None:
        """
        Insert node at end by default
        """
        if self.__head == None:
            self.__add___head(data=data)
            return
        new_node = node(data=data)
        last_node = self.__head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, data: str, after: str) -> None:
        '''
        Return after a speicif node
        '''
        if self.__head == None:
            self.__add___head(data=data)
            return
        new_node = node(data=data)
        req_node = self.__head
        while req_node.data != after:
            if not req_node.next:
                print("Data not found")
            req_node = req_node.next
        new_node.next = req_node.next
        new_node.prev = req_node
        req_node.next = new_node
        new_node.next.prev = new_node

    def delete_from_front(self) -> None:
        """
        Delete from the beginning of the list
        """
        if not self.__is_empty():
            self.__head = self.__head.next
            if self.__head:
                self.__head.prev = None

    def delete_from_end(self) -> None:
        """
        Delete from the end of the list
        """
        if not self.__is_empty():
            if self.__head.next == None:
                self.delete_from_front()
                return
            sec_last = None
            last_node = self.__head
            while last_node.next:
                sec_last = last_node
                last_node = last_node.next
            sec_last.next = None

    def delete_specific_node(self, data: str) -> None:
        """
        Delete node after a specific node
        """
        if not self.__is_empty():
            prev_node = None
            req_node = self.__head
            while req_node.data != data:
                if not req_node.next:
                    print("Data not found")
                    return
                prev_node = req_node
                req_node = req_node.next
            if self.__head.next == None:
                self.delete_from_front()
                return
            prev_node.next = req_node.next
            prev_node.prev = prev_node

    def traverse(self) -> None:
        if not self.__is_empty():
            nodes = []
            # print(self.__head)
            last_node = self.__head
            while last_node:
                nodes.append(last_node.data)
                last_node = last_node.next
            print(nodes)

    def get_list(self):
        return self.__head


if __name__ == "__main__":
    Linked_list = Single_Linked_List()
    while True:
        print(
            """
            1 - Insert at front
            2 - Insert at End
            3 - Insert after specific node
            4 - Traverse
            5 - Delete from front
            6 - Delete from end
            7 - Delete specified node
            8 - Exit
        """
        )
        try:
            choice = int(input("Choice : "))
            if choice == 4:
                Linked_list.traverse()
                continue
            print(f"Before : [{Linked_list.get_list()}]")
            if choice in [1, 2, 3, 7]:
                data_to_insert = input("Data : ")
                if choice == 1:
                    Linked_list.insert_at_front(data=data_to_insert)
                elif choice == 2:
                    Linked_list.insert_at_end(data=data_to_insert)
                elif choice == 3:
                    after_node = input("After which node : ")
                    Linked_list.insert_after_node(data=data_to_insert, after=after_node)
                elif choice == 7:
                    Linked_list.delete_specific_node(data=data_to_insert)
            elif choice == 5:
                Linked_list.delete_from_front()
            elif choice == 6:
                Linked_list.delete_from_end()
            elif choice == 8:
                break
            else:
                print("Incorrect option")
            print(f"After : [{Linked_list.get_list()}]")
            # _ = input()
        except ValueError:
            print("Incorrect Input")
