fatorial n = if n > 0 then n * fatorial (n - 1) else 1

main = do
  print(fatorial 5)
