#
# autor Maurício Freire
# Calcula o fatorial de um número.
# Calculates the fatorial of a number.

def fatorial(n)
    if n == 1 
        return 1
    end
    return n * fatorial(n - 1)
end

n = gets.chomp.to_i
puts "Fatorial de #{n} = #{fatorial(n)}"
