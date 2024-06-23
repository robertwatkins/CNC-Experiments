class tool:
  def __init__(self, number, info):
    self.number = number
    self.info = info

  def __str__(self):
    return "Tool: T" + str(self.number) + "-" + str(self.info)

class machine:
  def __init__(self, name, controller, startup, shutdown):
    self.name = name
    self.controller = controller
    self.startup = startup
    self.shutdown = shutdown
    
  def __str__(self):
    description = "Machine: Name-" + str(self.name) + ", Controller Type-" + str(self.controller)
    description += "\nStartup Commands: "
    for command in self.startup:
        description += "\n-" + command
    description += "\nShutdown Commands: "
    for command in self.shutdown:
        description += "\n-" + command
    return description

class project:
  def __init__(self, tools, machine):
    self.tools = tools
    self.machine = machine
    self.commands = []
    for command in self.machine.startup:
        self.commands.append(command)

  def __str__(self):
    description = ""
    for tool in self.tools:
        description += str(tool) + "\n"
    description += str(self.machine)
    description += "\nCommands"
    for command in self.commands:
        description += "\n" + command
    return description

  def finalize(self):
    for command in self.machine.shutdown:
        self.commands.append(command)


