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
