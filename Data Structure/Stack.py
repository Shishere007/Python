class stack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, data: str) -> bool:
        """
        Add element stro stack if not exist already
        """
        if data in self.__stack:
            return False
        self.__stack.append(data)
        return True

    def pop(self) -> (str, bool):
        """
        Remove and return the top element in the stack
        return false if empty
        """
        try:
            data = self.__stack.pop(-1)
            return data
        except Exception:
            return False

    def peek(self) -> (str, bool):
        """
        Peek at the top most element
        """
        try:
            return self.__stack[-1]
        except Exception:
            return False

    def traverse(self) -> None:
        print(self.__stack)

    def get_stack(self) -> list:
        """
        Return stack
        """
        return self.__stack


if __name__ == "__main__":
    Stack = stack()
    while True:
        print(
            """
            1 - PUSH
            2 - POP
            3 - PEEK
            4 - Traverse
            5 - Exit
        """
        )
        try:
            choice = int(input("Choice : "))
            if choice == 1:
                print(f"Before : {Stack.get_stack()}")
                Stack.push(data=input("Data to push : "))
                print(f"After : {Stack.get_stack()}")
            elif choice == 2:
                print(f"Before : {Stack.get_stack()}")
                data = Stack.pop()
                if data:
                    print(f"{data} poped from stack")
                else:
                    print("stack is empty")
                print(f"After : {Stack.get_stack()}")
            elif choice == 3:
                data = Stack.peek()
                if data:
                    print(f"Top element -> {data}")
                else:
                    print("Stack is empty")
            elif choice == 4:
                Stack.traverse()

            elif choice == 5:
                break
            else:
                print("Incorrect option")
            # _ = input()
        except ValueError:
            print("Incorrect Input")
