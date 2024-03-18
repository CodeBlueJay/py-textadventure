# Blue is a programming language that is designed by CodeBlueJay and has a simple synyax.

class Blue:
    def __init__(self, code):
        self.code = code

    def check_syntax(self):
        lines = self.code.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line:
                if not (line.startswith('type.out("') and line.endswith('")')) and \
                   not (line.startswith('type.in("') and line.endswith('")')) and \
                   not (line.startswith('if ') and line.endswith(':')) and \
                   not (line.startswith('repeat ') and line.endswith(':')):
                    raise SyntaxError(f"Syntax error in line {i}: {line}")

    def run(self, code=None):
        if code is None:
            self.check_syntax()
            code = self.code
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line:
                if line.startswith('type.out("') and line.endswith('")'):
                    print(line[10:-2])
                elif line.startswith('type.in("') and line.endswith('")'):
                    input(line[9:-2])
                elif line.startswith('if ') and line.endswith(':'):
                    condition = line[3:-1]
                    if eval(condition):
                        j = i + 1
                        while j < len(lines) and lines[j].startswith('    '):
                            j += 1
                        self.run('\n'.join(lines[i+1:j]))
                        i = j - 1
                elif line.startswith('repeat '):
                    times = int(line.split(' ', 1)[1][:-1])
                    j = i + 1
                    while j < len(lines) and lines[j].startswith('    '):
                        j += 1
                    for _ in range(times):
                        self.run('\n'.join(lines[i+1:j]))
                    i = j - 1
            i += 1

blue_code = """
type.out("Hello World")
repeat 2:
    type.out("Chat with me")
"""

interpreter = Blue(blue_code)
try:
    interpreter.run()
except SyntaxError as e:
    print(e)