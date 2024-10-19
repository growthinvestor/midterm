import cmd
from calculator import core, history

class CalculatorREPL(cmd.Cmd):
    prompt = '> '
    
    def do_add(self, args):
        """Add two numbers: add 2 3"""
        try:
            a, b = map(float, args.split())
            print(core.add(a, b))
        except Exception as e:
            print(f"Error: {e}")

    def do_subtract(self, args):
        """Subtract two numbers: subtract 5 2"""
        try:
            a, b = map(float, args.split())
            print(core.subtract(a, b))
        except Exception as e:
            print(f"Error: {e}")

    def do_history(self, _):
        """Display the history of calculations."""
        print(history.get_history())

    def do_exit(self, _):
        """Exit the calculator."""
        return True

if __name__ == '__main__':
    CalculatorREPL().cmdloop()
