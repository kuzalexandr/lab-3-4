import time
import contextlib
# Вариант 1: с использованием класса
class cm_timer_1:
  def __enter__(self):
    self.start = time.time()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    end = time.time()
    print(f"time: {end - self.start}")

# Вариант 2: с использованием contextlib
@contextlib.contextmanager
def cm_timer_2():
  start = time.time()
  yield
  end = time.time()
  print(f"time: {end - start}")