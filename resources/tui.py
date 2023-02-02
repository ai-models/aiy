import textual

def set_config_option():
    options = ['Option 1', 'Option 2', 'Option 3']
    selected_option = textual.select("Select an option:", options)
    print(f"You selected: {selected_option}")

if __name__ == '__main__':
    set_config_option()