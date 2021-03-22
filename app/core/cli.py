from .warehouse import Warehouse


def main():
    print("----------Welcome to Warehouse Management System------------")
    warehouse = Warehouse()
    print("Available options: \n"
          "1. Add new container \n"
          "2. Total container available \n"
          "3. Ship container ")

    while True:
        try:
            user_choice = int(input("Enter your choice(-1 to exit): "))
        except ValueError:
            print("Choice should be an integer value!! Please try again..")
            continue
        if user_choice == -1:
            print("Bye!!")
            break

        if user_choice == 1:
            print('Enter container type based on available choices')
            for index, cls in enumerate(warehouse.containertypes):
                print(f'{index + 1}. {cls.__name__}')

            c_choice = int(input('Enter container number: '))
            if (c_choice - 1) not in range(len(warehouse.containertypes)):
                print("please enter valid choice")
                continue
            warehouse.add_container(c_choice - 1)

        elif user_choice == 2:
            if warehouse.inventory:
                warehouse.display_inventory()
            else:
                print("No Containers available")

        elif user_choice == 3:
            container_id = input("Enter container id to deliver: ")
            position = warehouse.search_container(int(container_id))
            if position is not None:
                container = warehouse.remove_container(position)
                container.deliver()
            else:
                print('container id does not identified')

        else:
            print("please provide valid option")
