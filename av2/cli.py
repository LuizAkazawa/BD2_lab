class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class TeacherCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_person)
        self.add_command("read", self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_person(self):
        name = input("Enter the name: ")
        ano_nasc = int(input("Enter the ano_nascimento: "))
        cpf = input("Enter the CPF: ")
        self.person_model.create_teacher(name=name, ano_nasc=ano_nasc, cpf=cpf)

    def read_person(self):
        name = input("Enter the name: ")
        person = self.person_model.read_teacher(name)
        print(person)

    def update_person(self):
        name = input("Enter the name: ")
        cpf = input("Enter the cpf: ")
        self.person_model.update_teacher(name, cpf)

    def delete_person(self):
        name = input("Enter the name: ")
        self.person_model.delete_teacher(name)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
