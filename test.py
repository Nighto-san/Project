from icecream import ic
def test(func_name, args, expected_answers):
  """
  Тестирует функцию с заданными аргументами и ожидаемыми ответами.

  Args:
    func_name: Строка, имя тестируемой функции.
    args: Список аргументов для функции.
    expected_answers: Список ожидаемых ответов.
  """

  import sys
  module_name = sys._getframe(1).f_globals['__name__']
  module = sys.modules[module_name]
  func = getattr(module, func_name)

  for i, arg in enumerate(args):
    ic.includeContext
    try:
      result = func(arg)
    except Exception as e:
      print(f"📛 Ошибка для аргумента '{arg}': {e}")
    else:
      expected = expected_answers[i]
      if result == expected:
        print(f"✅  {expected} 🔀 {result}   Для аргумента '{arg}'")
      else:
        print(f"❌  {expected} 🔀 {result}   Для аргумента '{arg}'")

def parse(text):
  funk_name = re.search(r"(w+)(", text).group(1)
  args = re.findall(r"((d+,s*d+))", text)
  args = [tuple(map(int, arg.split(","))) for arg in args]
  expect = re.findall(r"[(.*?)]", text)
  expect = [eval(item) for item in expect]  # Осторожно: eval() может быть небезопасен
  return {'funk_name': funk_name, 'args': args, 'expect': expect}