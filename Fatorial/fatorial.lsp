;
; autor Maurício Freire
; Cálculo do fatorial de um número.
; Calculation of the factorial of a number.

(setq n (read))
(defun fatorial (n) (if (= n 0) 1 (* n (fatorial (- n 1)))))
(write (fatorial n))

