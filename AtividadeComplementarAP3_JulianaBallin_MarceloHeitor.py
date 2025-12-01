class TuringMachine:
  def __init__(self, tape):
      self.tape = list(tape) + [' ']*100  
      self.head = 0
      self.state = 'q0'
      self.transitions = {
          'q0': {'I': ('I', 'R', 'q1')},
          'q1': {'I': ('I', 'R', 'q1'), '#': ('#', 'R', 'q2')},
          'q2': {'I': ('I', 'R', 'q3')},
          'q3': {'I': ('I', 'R', 'q3'), '#': ('#', 'R', 'q4'), '=': ('=', 'R', 'q14')},
          'q4': {'I': ('I', 'R', 'q9'), '0': ('0', 'L', 'q5'), '=': ('=', 'L', 'q4')},
          'q5': {'I': ('I', 'L', 'q6'), '0': ('0', 'L', 'q5')},
          'q6': {'0': ('0', 'L', 'q6'), 'I': ('I', 'R', 'q17'), '#': ('#', 'R', 'q4')},
          'q7': {'0': ('0', 'R', 'q13')},
          'q8': {'I': ('I', 'R', 'q8'), '#': ('#', 'R', 'q9')},
          'q9': {'I': ('I', 'R', 'q9'), '0': ('0', 'R', 'q7'), '#': ('#', 'R', 'q4'), '=': ('=', 'L', 'q4')},
          'q10': {'I': ('I', 'R', 'q11'), '#': ('#', 'R', 'q4')},
          'q11': {'I': ('I', 'R', 'q10')},
          'q12': {'0': ('0', 'R', 'q12'), '=': ('=', 'R', 'q13')},
          'q13': {'0': ('0', 'R', 'q14')},
          'q14': {'I': ('I', 'R', 'q14'), '0': ('0', 'L', 'q15')},
          'q15': {'I': ('I', 'L', 'q15'), '=': ('=', 'L', 'q16')},
          'q16': {'=': ('=', 'L', 'q4')},
          'q17': {'I': ('I', 'R', 'q8'), '0': ('0', 'R', 'q12')},
          'q_accept': {' ': (' ', 'R', 'qA1')},
          'qA1': {' ': ('A', 'R', 'qA2')},
          'qA2': {' ': ('C', 'R', 'qA3')},
          'qA3': {' ': ('E', 'R', 'qA4')},
          'qA4': {' ': ('I', 'R', 'qA5')},
          'qA5': {' ': ('T', 'R', 'qA6')},
          'qA6': {' ': ('A', 'R', 'HALT')},
          'q_reject': {' ': ('R', 'R', 'qR1')},
          'qR1': {' ': ('E', 'R', 'qR2')},
          'qR2': {' ': ('J', 'R', 'qR3')},
          'qR3': {' ': ('E', 'R', 'qR4')},
          'qR4': {' ': ('I', 'R', 'qR5')},
          'qR5': {' ': ('T', 'R', 'qR6')},
          'qR6': {' ': ('A', 'R', 'qR7')},
          'qR7': {' ': (' ', 'R', 'HALT')},
          'HALT': {}
      }

  def step(self):
      current_char = self.tape[self.head] if self.head < len(self.tape) else ' '
      if self.state in self.transitions and current_char in self.transitions[self.state]:
          write_char, move, next_state = self.transitions[self.state][current_char]
          if self.head < len(self.tape):
              self.tape[self.head] = write_char
          else:
              self.tape.append(write_char)
          if move == 'R':
              self.head += 1
          elif move == 'L':
              self.head -= 1
          self.state = next_state
      else:
          if self.state in ['q3', 'q13', 'q14']:  # Accept states
              return "ACEITA"
          else:  # Reject in other states
              return "REJEITA"
      return None

  def run(self):
      while True:
          result = self.step()
          if result is not None:
              return result

def main():
  fita = input().strip()
  tm = TuringMachine(fita)
  resultado = tm.run()
  if resultado == "ACEITA":
      parts = fita.split('#')
      x = parts[0]
      y = parts[1]
      num_x = len(x)
      num_y = len(y)
      remainder = num_x % num_y
      result_string = f"{fita}={'I' * remainder} {resultado}"
  else:
      result_string = f"{fita} {resultado}"
  print(result_string)

if __name__ == "__main__":
  main()
