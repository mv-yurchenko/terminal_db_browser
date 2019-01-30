import readline

MAC_BINDING = "bind ^I rl_complete"
NORMAL_BINDING = "tab: complete"

def we_are_running_mac():
    return False

def set_autocomplete_with(bindings):
    readline.parse_and_bind(bindings)
commands = []

if we_are_running_mac():
    set_autocomplete_with(MAC_BINDING)
else:
    set_autocomplete_with(NORMAL_BINDING)

def completer(text, cmd_index):
    possible_commands = [cmd for cmd in commands if cmd.startswith(text)]
    if cmd_index < len(possible_commands):
        return possible_commands[cmd_index]
    else:
        return None

readline.set_completer(completer)

input_str = ""

while input_str != "exit":
    input_str = input('> ')
    commands.append(input_str)
    print(commands)